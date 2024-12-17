from csdl import get_connection
def gettongsach():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM Sach"
        cursor.execute(query)
        tongsachs = cursor.fetchone()[0]  
        print(f"Tổng số sách: {tongsachs}") 
        return tongsachs
    except Exception as e:
        print(f"Lỗi khi đếm tổng số sách: {e}")
        return 0 
    finally:
        if conn:
            conn.close()

def gettongloaisach():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM LoaiSach"
        cursor.execute(query)
        tongloaisachs = cursor.fetchone()[0]  
        print(f"Tổng số loại sách: {tongloaisachs}") 
        return tongloaisachs
    except Exception as e:
        print(f"Lỗi khi đếm tổng số loại sách: {e}")
        return 0 
    finally:
        if conn:
            conn.close()

def gettongtacgia():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM TacGia"
        cursor.execute(query)
        tongtacgias = cursor.fetchone()[0]  
        print(f"Tổng số tác giả: {tongtacgias}") 
        return tongtacgias
    except Exception as e:
        print(f"Lỗi khi đếm tổng số tác giả: {e}")
        return 0 
    finally:
        if conn:
            conn.close()

def gettongnhaxuatban():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM NhaXuatBan"
        cursor.execute(query)
        tongnhaxuatbans = cursor.fetchone()[0]  
        print(f"Tổng số nhà xuất bản: {tongnhaxuatbans}") 
        return tongnhaxuatbans
    except Exception as e:
        print(f"Lỗi khi đếm tổng số nhà xuất bản: {e}")
        return 0 
    finally:
        if conn:
            conn.close()

def gettongsinhvien():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM SinhVien"
        cursor.execute(query)
        tongsinhviens = cursor.fetchone()[0]  
        print(f"Tổng số sinh viên: {tongsinhviens}") 
        return tongsinhviens
    except Exception as e:
        print(f"Lỗi khi đếm tổng số sinh viên: {e}")
        return 0 
    finally:
        if conn:
            conn.close()

def gettongsachmuon():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM MuonTraSach"
        cursor.execute(query)
        tongsachmuons = cursor.fetchone()[0]  
        print(f"Tổng số sách mượn: {tongsachmuons}") 
        return tongsachmuons
    except Exception as e:
        print(f"Lỗi khi đếm tổng số sách mượn: {e}")
        return 0 
    finally:
        if conn:
            conn.close()

def gettongnhanvien():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM NhanVien"
        cursor.execute(query)
        tongnhanviens = cursor.fetchone()[0]  
        print(f"Tổng số nhân viên: {tongnhanviens}") 
        return tongnhanviens
    except Exception as e:
        print(f"Lỗi khi đếm tổng số nhân viên: {e}")
        return 0 
    finally:
        if conn:
            conn.close()

