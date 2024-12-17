from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from model.quanlynhanvien_model import getnhanvien, themnhanvien, suanhanvien, xoanhanvien,check_login

quanlynhanvien_bp = Blueprint('quanlynhanvien', __name__, url_prefix='/quanlynhanvien')

@quanlynhanvien_bp.route('/')
def get_quanlynhanvien():
    quanlynhanviens = getnhanvien()
    return render_template('quanlynhanvien.html', quanlynhanviens = quanlynhanviens)

@quanlynhanvien_bp.route('/them', methods=['POST'])
def them_quanlynhanvien():
    maNhanVien = request.form.get('maNhanVien')
    tenNhanVien = request.form.get('tenNhanVien')
    soDienThoai = request.form.get('soDienThoai')
    gioiTinh = request.form.get('gioiTinh')
    diaChi = request.form.get('diaChi')
    matKhau = request.form.get('matKhau')
    vaiTro = request.form.get('vaiTro')

    if not maNhanVien:
        flash('Vui lòng nhập mã nhân viên', 'danger')
        return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))
    if not tenNhanVien:
        flash('Vui lòng nhập tên nhân viên', 'danger')
        return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))
    if not soDienThoai:
        flash('Vui lòng nhập số điện thoại', 'danger')
        return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))
    if len(soDienThoai) != 10 or not soDienThoai.isdigit() or soDienThoai[0] != '0':
        flash('Số điện thoại phải là 10 số và bắt đầu bằng số 0.', 'danger')
        return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))
    if not diaChi:
        flash('Vui lòng nhập địa chỉ', 'danger')
        return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))
    if not matKhau:
        flash('Vui lòng nhập mật khẩu', 'danger')
        return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))

    message = themnhanvien(maNhanVien, tenNhanVien, soDienThoai, gioiTinh, diaChi, matKhau, vaiTro)
    if message == "Mã nhân viên đã tồn tại":
        flash(message, 'danger')
    elif message == "Thêm nhân viên thành công!":
        flash(message, 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))

@quanlynhanvien_bp.route('/sua', methods=['POST'])
def sua_quanlynhanvien():
    maNhanVien = request.form.get('maNhanVien')
    tenNhanVien = request.form.get('tenNhanVien')
    soDienThoai = request.form.get('soDienThoai')
    gioiTinh = request.form.get('gioiTinh')
    diaChi = request.form.get('diaChi')
    matKhau = request.form.get('matKhau')
    vaiTro = request.form.get('vaiTro')

    if not maNhanVien:
        flash('Vui lòng nhập mã nhân viên', 'danger')
        return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))
    if not tenNhanVien:
        flash('Vui lòng nhập tên nhân viên', 'danger')
        return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))
    if not soDienThoai:
        flash('Vui lòng nhập số điện thoại', 'danger')
        return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))
    if not diaChi:
        flash('Vui lòng nhập địa chỉ', 'danger')
        return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))
    if not matKhau:
        flash('Vui lòng nhập mật khẩu', 'danger')
        return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))
    if len(soDienThoai) != 10 or not soDienThoai.isdigit() or soDienThoai[0] != '0':
        flash('Số điện thoại phải là 10 số và bắt đầu bằng số 0.', 'danger')
        return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))

    message = suanhanvien(maNhanVien, tenNhanVien, soDienThoai, gioiTinh, diaChi, matKhau, vaiTro)
    if message == "Mã nhân viên không tồn tại":
        flash(message, 'danger') 
    else:
        flash('Cập nhật nhân viên thành công!', 'success') 
    return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))

@quanlynhanvien_bp.route('/xoa/<maNhanVien>', methods=['POST'])
def xoa_quanlynhanvien(maNhanVien):
    message = xoanhanvien(maNhanVien)
    if message == "Xóa nhân viên thành công!":
        flash(message, 'success')
    else:
        flash(message, 'danger') 
    return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))

@quanlynhanvien_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone = request.form['phone']
        password = request.form['password']
        user = check_login(phone, password)
        
        if user:
            session['logged_in'] = True
            session['user_id'] = user[0] 
            session['user_name'] = user[1] 
            session['role'] = user[2]

            print(f"User ID: {session['user_id']}, Role: {session['role']}")
            if user[2] == 'admin':
                return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))
            else:
                return redirect(url_for('home'))
        else:
            return render_template('dangnhap.html', error="Số điện thoại hoặc mật khẩu không đúng")
    return render_template('dangnhap.html')

@quanlynhanvien_bp.route('/logout')
def logout():
    session.clear() 
    return redirect(url_for('quanlynhanvien.login'))
