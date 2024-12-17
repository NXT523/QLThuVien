from csdl import get_connection
from datetime import datetime

def getmuontrasach():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT MS.MaPhieuMuon, SV.MaSV, SV.TenSV, S.MaSach, S.TenSach, 
               FORMAT(MS.NgayMuon, 'dd/MM/yyyy') AS NgayMuon, 
               FORMAT(MS.NgayTra, 'dd/MM/yyyy') AS NgayTra, 
               MS.GhiChu
        FROM MuonTraSach MS
        JOIN Sach S ON S.MaSach = MS.MaSach
        JOIN SinhVien SV ON SV.MaSV = MS.MaSV
        """
        cursor.execute(query)
        muontrasachs = cursor.fetchall()
        print("Dữ liệu mượn trả sách đã được truy xuất với định dạng ngày.")
        return muontrasachs
    except Exception as e:
        print(f"Lỗi khi lấy dữ liệu mượn trả sách: {e}")
        return []
    finally:
        if conn:
            conn.close()

def muonsach(txtMaSV, txtMaSach, txtNgayMuon, txtNgayTra, txtGhiChu):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # Kiểm tra sinh viên đã mượn quyển sách này chưa
        query_check_duplicate_loan = """
        SELECT MaSV 
        FROM MuonTraSach 
        WHERE MaSV = ? AND MaSach = ?
        """
        cursor.execute(query_check_duplicate_loan, (txtMaSV, txtMaSach))
        existing_loan = cursor.fetchone()

        if existing_loan:
            ma_sv_da_muon = existing_loan[0]
            return f"error: {ma_sv_da_muon} đã mượn quyển sách này rồi"
        
        # Kiểm tra số lượng mượn tối đa 3 quyển
        query_check_borrowed = """
        SELECT COUNT(*) 
        FROM MuonTraSach 
        WHERE MaSV = ? 
        """
        cursor.execute(query_check_borrowed, (txtMaSV,))
        borrowed_count = cursor.fetchone()[0]

        if borrowed_count >= 3:
            return "error: Sinh viên đã mượn quá 3 cuốn sách chưa trả"
        
        # Kiểm tra số lượng sách còn trong thư viện
        query_check_book = """
        SELECT SoLuong 
        FROM Sach 
        WHERE MaSach = ?
        """
        cursor.execute(query_check_book, (txtMaSach,))
        result = cursor.fetchone()
        if not result:
            return "error: Sách không tồn tại"
        if result[0] <= 0:
            return "error: Sách không còn sẵn để mượn"

        # Chuyển đổi ngày mượn và ngày trả
        ngay_muon_formatted = datetime.strptime(txtNgayMuon, "%d/%m/%Y")
        ngay_tra_formatted = datetime.strptime(txtNgayTra, "%d/%m/%Y") if txtNgayTra else None

        # Kiểm tra mượn sách không được quá ngày mượn quá 90 ngày
        if ngay_tra_formatted:
            days_diff = (ngay_tra_formatted - ngay_muon_formatted).days
            if days_diff > 90:
                return "error: Thời gian mượn sách không được vượt quá 90 ngày"

        # Thêm phiếu mượn vào CSDL MuonTraSach
        query_insert_loan = """
        INSERT INTO MuonTraSach (MaSV, MaSach, NgayMuon, NgayTra, GhiChu)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(
            query_insert_loan,
            (txtMaSV, txtMaSach, ngay_muon_formatted.strftime("%Y-%m-%d"),
             ngay_tra_formatted.strftime("%Y-%m-%d") if ngay_tra_formatted else None, txtGhiChu)
        )
        conn.commit()

        # Giảm số lượng sách đi 1
        query_update_books = """
        UPDATE Sach 
        SET SoLuong = SoLuong - 1 
        WHERE MaSach = ?
        """
        cursor.execute(query_update_books, (txtMaSach,))
        conn.commit()
        return "Mượn sách thành công"
    except Exception as e:
        print(f"Lỗi khi mượn sách: {e}")
        if conn:
            conn.rollback()
        return f"error: {e}"
    finally:
        if conn:
            conn.close()

def trasach(maPhieuMuon):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query_get_book = "SELECT MaSach FROM MuonTraSach WHERE MaPhieuMuon = ?"
        cursor.execute(query_get_book, (maPhieuMuon,))
        result = cursor.fetchone()
        if not result:
            return "error: loan record not found"
        maSach = result[0]

        # Xóa phiếu mượn trong CSDL
        query_delete_loan = "DELETE FROM MuonTraSach WHERE MaPhieuMuon = ?"
        cursor.execute(query_delete_loan, (maPhieuMuon,))
        conn.commit()

        # Tăng số lượng sách thêm 1
        query_update_book = "UPDATE Sach SET SoLuong = SoLuong + 1 WHERE MaSach = ?"
        cursor.execute(query_update_book, (maSach,))
        conn.commit()
        return "success: book returned"
    except Exception as e:
        conn.rollback()
        return f"error: {e}"
    finally:
        if conn:
            conn.close()

def giahan_ngaytra(maPhieuMuon, ngayTraMoi):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        try:
            ngayTraMoi_formatted = datetime.strptime(ngayTraMoi, "%d/%m/%Y")
        except ValueError:
            return "error: Ngày trả mới không đúng định dạng (DD/MM/YYYY)"

        # Kiểm tra ngày gia hạn không vượt quá 90 ngày tính từ ngày hiện tại
        today = datetime.now()
        days_difference = (ngayTraMoi_formatted - today).days
        if days_difference > 90:
            return "error: Ngày gia hạn không được vượt quá 90 ngày tính từ ngày hiện tại"

        # Kiểm tra rằng ngày trả mới phải lớn hơn ngày hiện tại
        if ngayTraMoi_formatted <= today:
            return "error: Ngày trả mới phải lớn hơn ngày hiện tại"

        # Cập nhật ngày trả về trong CSDLCSDL
        query_update_date = """
        UPDATE MuonTraSach 
        SET NgayTra = ? 
        WHERE MaPhieuMuon = ?
        """
        cursor.execute(query_update_date, (ngayTraMoi_formatted.strftime("%Y-%m-%d"), maPhieuMuon))
        conn.commit()
        return "success: Gia hạn ngày trả thành công"
    except Exception as e:
        if conn:
            conn.rollback()
        return f"error: {str(e)}"
    finally:
        if conn:
            conn.close()
