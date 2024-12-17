from csdl import get_connection

def getquanlysach():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT 
            S.MaSach,
            S.TenSach,
            LS.TenLoaiSach,
            NXB.TenNXB AS NhaXuatBan,
            TG.TenTacGia AS TacGia,
            S.SoTrang,
            S.GiaBan,
            S.SoLuong,
            S.HinhAnh
        FROM 
            Sach S
        JOIN 
            LoaiSach LS ON S.MaLoai = LS.MaLoai
        JOIN 
            NhaXuatBan NXB ON S.MaNXB = NXB.MaNXB
        JOIN 
            TacGia TG ON S.MaTacGia = TG.MaTacGia;
        """
        cursor.execute(query)
        quanlysachs = cursor.fetchall()
        return quanlysachs

    except Exception as e:
        print("Lỗi khi truy vấn dữ liệu từ cơ sở dữ liệu:", e)
        return None

    finally:
        if conn:
            conn.close()
