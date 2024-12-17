from csdl import get_connection

def getnhanvien():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """SELECT * FROM NhanVien"""
        cursor.execute(query)
        nhanviens = cursor.fetchall()
        return nhanviens
    except Exception as e:
        print("Lỗi khi truy vấn dữ liệu từ cơ sở dữ liệu:", e)
        return None
    finally:
        if conn:
            conn.close()

def themnhanvien(txtMaNhanVien, txtTenNhanVien, txtSoDienThoai, txtGioiTinh, txtDiaChi, txtMatkhau, txtVaiTro):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        check_query = "SELECT COUNT(*) FROM NhanVien WHERE MaNhanVien = ?"
        cursor.execute(check_query, (txtMaNhanVien))
        if cursor.fetchone()[0] > 0:
            return "Mã nhân viên đã tồn tại"

        check_query_sdt = "SELECT COUNT(*) FROM NhanVien WHERE SoDienThoai = ?"
        cursor.execute(check_query_sdt, (txtSoDienThoai,))
        if cursor.fetchone()[0] > 0:
            return "Số điện thoại đã được sử dụng"

        query = """
            INSERT INTO NhanVien (MaNhanVien, TenNhanVien, SoDienThoai, GioiTinh, DiaChi, MatKhau, VaiTro) VALUES (?, ?, ?, ?, ?, ?, ?)
            """
        cursor.execute(query, (txtMaNhanVien, txtTenNhanVien, txtSoDienThoai, txtGioiTinh, txtDiaChi, txtMatkhau, txtVaiTro))
        conn.commit()
        return "Thêm nhân viên thành công!"

    except Exception as e:
        print("Lỗi khi thêm dữ liệu vào cơ sở dữ liệu:", e)
        return "Lỗi khi thêm nhân viên"

    finally:
        if conn:
            conn.close()

def suanhanvien(txtMaNhanVien, txtTenNhanVien, txtSoDienThoai, txtGioiTinh, txtDiaChi, txtMatkhau, txtVaiTro):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        check_query = "SELECT COUNT(*) FROM NhanVien WHERE MaNhanVien = ?"
        cursor.execute(check_query, (txtMaNhanVien,))
        if cursor.fetchone()[0] == 0:
            return "Mã nhân viên không tồn tại"
        
        check_query_sdt = "SELECT COUNT(*) FROM NhanVien WHERE SoDienThoai = ?"
        cursor.execute(check_query_sdt, (txtSoDienThoai,))
        if cursor.fetchone()[0] > 0:
            return "Số điện thoại đã được sử dụng"
        
        query = """
        UPDATE NhanVien
        SET TenNhanVien = ?, SoDienThoai = ?, GioiTinh = ?, DiaChi = ?, MatKhau = ?, VaiTro = ?
        WHERE MaNhanVien = ?
        """
        cursor.execute(query, (txtTenNhanVien, txtSoDienThoai, txtGioiTinh, txtDiaChi, txtMatkhau, txtVaiTro, txtMaNhanVien))
        conn.commit()
        return "Cập nhật nhân viên thành công!"

    except Exception as e:
        print("Lỗi khi cập nhật dữ liệu trong cơ sở dữ liệu:", e)
        return "Lỗi khi cập nhật nhân viên"

    finally:
        if conn:
            conn.close()

def xoanhanvien(maNhanVien):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM NhanVien WHERE MaNhanVien = ?"
        cursor.execute(query, (maNhanVien,))
        conn.commit()
        return "Xóa nhân viên thành công!"

    except Exception as e:
        if "foreign key constraint" in str(e).lower():
            return " không thể xóa."
        else:
            print("Lỗi khi xóa dữ liệu từ cơ sở dữ liệu:", e)
            return "Xóa không thành công do tồn tại nhân viên trong bảng sách."

    finally:
        if conn:
            conn.close()

def check_login(phone, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MaNhanVien, TenNhanVien, VaiTro FROM NhanVien WHERE SoDienThoai = ? AND MatKhau = ?", (phone, password))
    user = cursor.fetchone()
    return user
