from flask import Blueprint, request, render_template, redirect, url_for, flash
from model.quanlysinhvien_model import getsinhvien, themsinhvien, suasinhvien, xoasinhvien

quanlysinhvien_bp = Blueprint('quanlysinhvien', __name__, url_prefix='/quanlysinhvien')

@quanlysinhvien_bp.route('/')
def get_quanlysinhvien():
    quanlysinhviens = getsinhvien()
    return render_template('quanlysinhvien.html', quanlysinhviens=quanlysinhviens)

@quanlysinhvien_bp.route('/them', methods=['POST'])
def them_quanlysinhvien():
    maSinhVien = request.form.get('maSinhVien')
    tenSinhVien = request.form.get('tenSinhVien')
    nganhHoc = request.form.get('nganhHoc')
    khoaHoc = request.form.get('khoaHoc')
    soDienThoai = request.form.get('soDienThoai')

    if not maSinhVien:
        flash('Vui lòng nhập mã sinh viên', 'danger')
        return redirect(url_for('quanlysinhvien.get_quanlysinhvien'))
    if not tenSinhVien:
        flash('Vui lòng nhập tên sinh viên', 'danger')
        return redirect(url_for('quanlysinhvien.get_quanlysinhvien'))
    if not nganhHoc:
        flash('Vui lòng nhập ngành học', 'danger')
        return redirect(url_for('quanlysinhvien.get_quanlysinhvien'))
    if not khoaHoc:
        flash('Vui lòng nhập khóa học', 'danger')
        return redirect(url_for('quanlysinhvien.get_quanlysinhvien'))
    if not soDienThoai:
        flash('Vui lòng nhập số điện thoại', 'danger')
        return redirect(url_for('quanlysinhvien.get_quanlysinhvien'))
    if len(soDienThoai) != 10 or not soDienThoai.isdigit():
        flash('Số điện thoại phải là 10 số và chỉ chứa chữ số.', 'danger')
        return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))
    
    message = themsinhvien(maSinhVien, tenSinhVien, nganhHoc, khoaHoc, soDienThoai)
    if message == "Mã sinh vien đã tồn tại":
        flash(message, 'danger')
    elif message == "Thêm sinh vien thành công!":
        flash(message, 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('quanlysinhvien.get_quanlysinhvien'))

@quanlysinhvien_bp.route('/sua', methods=['POST'])
def sua_quanlysinhvien():
    maSinhVien = request.form.get('maSinhVien')
    tenSinhVien = request.form.get('tenSinhVien')
    nganhHoc = request.form.get('nganhHoc')
    khoaHoc = request.form.get('khoaHoc')
    soDienThoai = request.form.get('soDienThoai')
    
    if not maSinhVien:
        flash('Vui lòng nhập mã sinh viên', 'danger')
        return redirect(url_for('quanlysinhvien.get_quanlysinhvien'))
    if not tenSinhVien:
        flash('Vui lòng nhập tên sinh viên', 'danger')
        return redirect(url_for('quanlysinhvien.get_quanlysinhvien'))
    if not nganhHoc:
        flash('Vui lòng nhập ngành học', 'danger')
        return redirect(url_for('quanlysinhvien.get_quanlysinhvien'))
    if not khoaHoc:
        flash('Vui lòng nhập khóa học', 'danger')
        return redirect(url_for('quanlysinhvien.get_quanlysinhvien'))
    if not soDienThoai:
        flash('Vui lòng nhập số điện thoại', 'danger')
        return redirect(url_for('quanlysinhvien.get_quanlysinhvien'))
    if len(soDienThoai) != 10 or not soDienThoai.isdigit():
        flash('Số điện thoại phải là 10 số và chỉ chứa chữ số.', 'danger')
        return redirect(url_for('quanlynhanvien.get_quanlynhanvien'))

    message = suasinhvien(maSinhVien, tenSinhVien, nganhHoc, khoaHoc, soDienThoai)
    if message == "Mã sinh viên không tồn tại":
        flash(message, 'danger') 
    else:
        flash('Cập nhật sinh viên thành công!', 'success') 
    return redirect(url_for('quanlysinhvien.get_quanlysinhvien'))

@quanlysinhvien_bp.route('/xoa/<maSinhVien>', methods=['POST'])
def xoa_quanlysinhvien(maSinhVien):
    message = xoasinhvien(maSinhVien)

    if message == "Xóa sinh vien thành công!":
        flash(message, 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('quanlysinhvien.get_quanlysinhvien'))


