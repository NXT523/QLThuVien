from csdl import get_connection

def getdanhsachdangmuon():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT MS.MaPhieuMuon, SV.MaSV, SV.TenSV, SV.SoDienThoai, 
        S.TenSach, 
        FORMAT(MS.NgayMuon, 'dd/MM/yyyy') AS NgayMuon, 
        FORMAT(MS.NgayTra, 'dd/MM/yyyy') AS NgayTra, 
        MS.GhiChu
        FROM MuonTraSach MS
        JOIN Sach S ON S.MaSach = MS.MaSach
        JOIN SinhVien SV ON SV.MaSV = MS.MaSV
        WHERE MS.NgayTra > CONVERT(date, GETDATE());

        """
        cursor.execute(query)
        danhsachdangmuons = cursor.fetchall()
        return danhsachdangmuons
    except Exception as e:
        print(f"Lỗi khi lấy danh sách đang mượn: {e}")
        return []
    finally:
        if conn:
            conn.close()
