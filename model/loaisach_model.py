from csdl import get_connection

def getloaisach():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT * FROM LoaiSach
        """
        cursor.execute(query)
        loaisachs = cursor.fetchall()
        return loaisachs

    except Exception as e:
        print("Lỗi khi truy vấn dữ liệu từ cơ sở dữ liệu:", e)
        return None
    
    finally:
        if conn:
            conn.close()

def themloaisach(txtMaLoai, txtLoaiSach, txtGhiChu):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        check_query = "SELECT COUNT(*) FROM LoaiSach WHERE MaLoai = ?"
        cursor.execute(check_query, (txtMaLoai,))
        if cursor.fetchone()[0] > 0:
            return "Mã loại sách đã tồn tại"
        query = """
        INSERT INTO LoaiSach (MaLoai, TenLoaiSach, GhiChu)
        VALUES (?, ?, ?)
        """
        cursor.execute(query, (txtMaLoai, txtLoaiSach, txtGhiChu))
        conn.commit()
        return "Thêm loại sách thành công!"

    except Exception as e:
        print("Lỗi khi thêm dữ liệu vào cơ sở dữ liệu:", e)
        return "Lỗi khi thêm loại sách"

    finally:
        if conn:
            conn.close()

def sualoaisach(txtMaLoai, txtLoaiSach, txtGhiChu):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        check_query = "SELECT COUNT(*) FROM LoaiSach WHERE MaLoai = ?"
        cursor.execute(check_query, (txtMaLoai,))
        if cursor.fetchone()[0] == 0:
            return "Mã loại sách không tồn tại"
        query = """
        UPDATE LoaiSach
        SET TenLoaiSach = ?, GhiChu = ?
        WHERE MaLoai = ?
        """
        cursor.execute(query, (txtLoaiSach, txtGhiChu, txtMaLoai))
        conn.commit()
        print("Cập nhật loại sách thành công!")

    except Exception as e:
        print("Lỗi khi cập nhật dữ liệu trong cơ sở dữ liệu:", e)

    finally:
        if conn:
            conn.close()

def xoaloaisach(maLoai):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM LoaiSach WHERE MaLoai = ?"
        cursor.execute(query, (maLoai,))
        conn.commit()  
        return "Xóa loại sách thành công!"

    except Exception as e:
        if "foreign key constraint" in str(e).lower():
            return "Loại sách hiện đang được sử dụng trong bảng Sách, không thể xóa."
        else:
            print("Lỗi khi xóa dữ liệu từ cơ sở dữ liệu:", e)
            return "Xóa không thành công do tồn tại loại sách trong bảng sách."

    finally:
        if conn:
            conn.close()
