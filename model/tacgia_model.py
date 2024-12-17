from csdl import get_connection

def gettacgia():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT * FROM TacGia
        """
        cursor.execute(query)
        tacgias = cursor.fetchall()
        return tacgias

    except Exception as e:
        print("Lỗi khi truy vấn dữ liệu từ cơ sở dữ liệu:", e)
        return None

    finally:
        if conn:
            conn.close()

def themtacgia(txtMaTacGia, txtTenTacGia, txtGhiChu):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        check_query = "SELECT COUNT(*) FROM TacGia WHERE MaTacGia = ?"
        cursor.execute(check_query, (txtMaTacGia,))
        if cursor.fetchone()[0] > 0:
            return "Mã tác giả đã tồn tại"

        query = """
            INSERT INTO TacGia (MaTacGia, TenTacGia, GhiChu)
            VALUES (?, ?, ?)
            """
        cursor.execute(query, (txtMaTacGia, txtTenTacGia, txtGhiChu))
        conn.commit()
        return "Thêm tác giả thành công!"

    except Exception as e:
        print("Lỗi khi thêm dữ liệu vào cơ sở dữ liệu:", e)
        return "Lỗi khi thêm loại sách"

    finally:
        if conn:
            conn.close()

def suatacgia(txtMaTacGia, txtTenTacGia, txtGhiChu):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        check_query = "SELECT COUNT(*) FROM TacGia WHERE MaTacGia = ?"
        cursor.execute(check_query, (txtMaTacGia,))
        if cursor.fetchone()[0] == 0:
            return "Mã tác giả không tồn tại"

        query = """
        UPDATE TacGia
        SET TenTacGia = ?, GhiChu = ?
        WHERE MaTacGia = ?
        """
        cursor.execute(query, (txtTenTacGia, txtGhiChu, txtMaTacGia))
        conn.commit()
        return "Cập nhật tác giả thành công!"

    except Exception as e:
        print("Lỗi khi cập nhật dữ liệu trong cơ sở dữ liệu:", e)
        return "Lỗi khi cập nhật dữ liệu!"

    finally:
        if conn:
            conn.close()

def xoatacgia(maTacGia):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM TacGia WHERE MaTacGia = ?"
        cursor.execute(query, (maTacGia,))
        conn.commit()
        return "Xóa loại sách thành công!"

    except Exception as e:
        if "foreign key constraint" in str(e).lower():
            return "Loại sách hiện đang được sử dụng trong bảng Sách, không thể xóa."
        else:
            print("Lỗi khi xóa dữ liệu từ cơ sở dữ liệu:", e)
            return "Xóa không thành công do tồn tại tác giả trong bảng sách."

    finally:
        if conn:
            conn.close()
