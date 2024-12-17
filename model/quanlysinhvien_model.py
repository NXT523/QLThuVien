from csdl import get_connection

def getsinhvien():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT * FROM SinhVien
        """
        cursor.execute(query)
        sinhviens = cursor.fetchall()
        return sinhviens

    except Exception as e:
        print("Lỗi khi truy vấn dữ liệu từ cơ sở dữ liệu:", e)
        return None

    finally:
        if conn:
            conn.close()

def themsinhvien(txtMaSV, txtTenSV, txtNganhHoc, txtKhoaHoc, txtSoDienThoai):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        check_query = "SELECT COUNT(*) FROM SinhVien WHERE MaSV = ?"
        cursor.execute(check_query, (txtMaSV,))
        if cursor.fetchone()[0] > 0:
            return "Mã sinh vien đã tồn tại"

        check_query_sdt = "SELECT COUNT(*) FROM SinhVien WHERE SoDienThoai = ?"
        cursor.execute(check_query_sdt, (txtSoDienThoai,))
        if cursor.fetchone()[0] > 0:
            return "Số điện thoại đã được sử dụng"

        query = """
            INSERT INTO SinhVien (MaSV, TenSV, NganhHoc, KhoaHoc, SoDienThoai)
            VALUES (?, ?, ?, ?, ?)
            """
        cursor.execute(query, (txtMaSV, txtTenSV, txtNganhHoc, txtKhoaHoc, txtSoDienThoai))
        conn.commit()
        return "Thêm sinh viên thành công!"

    except Exception as e:
        print("Lỗi khi thêm dữ liệu vào cơ sở dữ liệu:", e)
        return "Lỗi khi thêm sinh viên"

    finally:
        if conn:
            conn.close()

def suasinhvien(txtMaSV, txtTenSV, txtNganhHoc, txtKhoaHoc, txtSoDienThoai):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        check_query = "SELECT COUNT(*) FROM SinhVien WHERE MaSV = ?"
        cursor.execute(check_query, (txtMaSV,))
        if cursor.fetchone()[0] == 0:
            return "Mã sinh viên không tồn tại"

        query = """
        UPDATE SinhVien
        SET TenSV = ?, NganhHoc = ?, KhoaHoc = ?, SoDienThoai = ?
        WHERE MaSV = ?
        """
        cursor.execute(query, (txtTenSV, txtNganhHoc, txtKhoaHoc,txtSoDienThoai,txtMaSV))
        conn.commit()
        return "Cập nhật sinh viên thành công!"
    
    except Exception as e:
        print("Lỗi khi cập nhật dữ liệu trong cơ sở dữ liệu:", e)

    finally:
        if conn:
            conn.close()

def xoasinhvien(maSinhVien):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM SinhVien WHERE MaSV = ?"
        cursor.execute(query, (maSinhVien,))
        conn.commit()
        return "Xóa sinh viên thành công!"

    except Exception as e:
        if "foreign key constraint" in str(e).lower():
            return "Sinh vien van dang muon sach, không thể xóa."
        else:
            print("Lỗi khi xóa dữ liệu từ cơ sở dữ liệu:", e)
            return "Xóa không thành công do tồn tại sinh vien trong bảng sách."
        
    finally:
        if conn:
            conn.close()
