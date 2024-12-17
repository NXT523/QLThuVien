from flask import Flask,render_template, send_from_directory
from routes.quanlysach_routes import quanlysach_bp
from routes.quanlysinhvien_routes import quanlysinhvien_bp
from routes.quanlymuontrasach_routes import quanlymuontrasach_bp
from routes.quanlynhanvien_routes import quanlynhanvien_bp
from routes.quanlybaocaothongke_routes import quanlybaocaothongke_bp
from routes.tacgia_routes import tacgia_bp
from routes.loaisach_routes import loaisach_bp
from routes.nhaxuatban_routes import nhaxuatban_bp
from routes.sach_routes import sach_bp
from routes.danhsachquahan_routes import danhsachquahan_bp
from routes.danhsachdangmuon_routes import danhsachdangmuon_bp

app = Flask(__name__)
app.secret_key = 'your_unique_secret_key_here'

app.register_blueprint(quanlysach_bp)
app.register_blueprint(quanlysinhvien_bp)
app.register_blueprint(quanlymuontrasach_bp)
app.register_blueprint(quanlynhanvien_bp)
app.register_blueprint(quanlybaocaothongke_bp)
app.register_blueprint(tacgia_bp)
app.register_blueprint(loaisach_bp)
app.register_blueprint(sach_bp)
app.register_blueprint(nhaxuatban_bp)
app.register_blueprint(danhsachdangmuon_bp)
app.register_blueprint(danhsachquahan_bp)

@app.route('/')
def index():
    return render_template('dangnhap.html')

@app.route('/home')
def home():
    return render_template('trangchu.html')

@app.route('/gioithieu')
def gioithieu():
    return  render_template(('gioithieu.html'))

@app.route('/login')
def login():
    return render_template('dangnhap.html')

@app.route('/anh/<filename>')
def duongdan_picture(filename):
    return send_from_directory('picture', filename)

if __name__ == '__main__':
    app.run(debug=True)
