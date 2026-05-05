import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QSlider, QPushButton, QFileDialog, 
                             QFrame, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QCheckBox)
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QImage, QPixmap, QPainter, QWheelEvent
from PIL import Image, ImageEnhance, ImageChops # 使用 ImageChops 代替 ImageMath

class ImagePreviewerView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.pixmap_item = QGraphicsPixmapItem()
        self.scene.addItem(self.pixmap_item)
        self.setStyleSheet("background-color: #202020; border: 1px solid #333; border-radius: 4px;")

    def set_image(self, qpixmap):
        self.pixmap_item.setPixmap(qpixmap)
        self.scene.setSceneRect(QRectF(qpixmap.rect()))

    def wheelEvent(self, event: QWheelEvent):
        zoom_in_factor = 1.15
        zoom_out_factor = 1 / zoom_in_factor
        if event.angleDelta().y() > 0:
            self.scale(zoom_in_factor, zoom_in_factor)
        else:
            self.scale(zoom_out_factor, zoom_out_factor)

    def mouseDoubleClickEvent(self, event):
        self.fit_image()

    def fit_image(self):
        if not self.pixmap_item.pixmap().isNull():
            self.resetTransform()
            self.fitInView(self.pixmap_item, Qt.KeepAspectRatio)

class ModernImageEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pro Image Editor v4.2")
        self.resize(1250, 850)
        
        self.original_image = None
        self.processed_image = None
        self._is_init = False 
        
        self.init_ui()
        self.apply_style()
        self._is_init = True

    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        self.view = ImagePreviewerView()
        main_layout.addWidget(self.view, stretch=5)

        control_frame = QFrame()
        control_frame.setFixedWidth(300)
        control_panel = QVBoxLayout(control_frame)
        
        self.btn_open = QPushButton("导入图片")
        self.btn_save = QPushButton("导出图片")
        self.btn_open.clicked.connect(self.load_image)
        self.btn_save.clicked.connect(self.save_image)
        control_panel.addWidget(self.btn_open)
        control_panel.addWidget(self.btn_save)
        control_panel.addSpacing(15)

        self.sliders = {}
        self.value_labels = {}
        
        controls = [
            ("亮度", 0, 200, 100),
            ("对比度", 0, 200, 100),
            ("灰度/饱和度", 0, 200, 100),
            ("色相旋转", 0, 360, 0),
            ("不透明度", 0, 100, 100),
        ]

        for label_text, min_v, max_v, def_v in controls:
            row = QHBoxLayout()
            row.addWidget(QLabel(label_text))
            v_lbl = QLabel(str(def_v))
            v_lbl.setStyleSheet("color: #0078d4; font-weight: bold;")
            row.addStretch()
            row.addWidget(v_lbl)
            control_panel.addLayout(row)

            slider = QSlider(Qt.Horizontal)
            slider.setRange(min_v, max_v)
            slider.setValue(def_v)
            slider.valueChanged.connect(self.update_image)
            control_panel.addWidget(slider)
            
            if label_text == "灰度/饱和度":
                self.cb_protect_white = QCheckBox("排除接近白色的像素")
                self.cb_protect_white.setStyleSheet("color: #888; font-size: 11px; padding-left: 5px;")
                self.cb_protect_white.stateChanged.connect(self.update_image)
                control_panel.addWidget(self.cb_protect_white)

            control_panel.addSpacing(12)
            self.sliders[label_text] = slider
            self.value_labels[label_text] = v_lbl

        control_panel.addStretch()
        main_layout.addWidget(control_frame, stretch=1)

    def apply_style(self):
        self.setStyleSheet("""
            QMainWindow { background-color: #121212; }
            QLabel { color: #ccc; font-family: 'Segoe UI', sans-serif; }
            QPushButton { 
                background-color: #2d2d2d; color: white; border: 1px solid #3d3d3d;
                padding: 12px; border-radius: 4px; font-weight: bold;
            }
            QPushButton:hover { background-color: #3d3d3d; border-color: #0078d4; }
            QCheckBox { color: #aaa; }
            QSlider::groove:horizontal { background: #2d2d2d; height: 4px; border-radius: 2px; }
            QSlider::handle:horizontal { background: #0078d4; width: 14px; height: 14px; margin: -5px 0; border-radius: 7px; }
        """)

    def load_image(self):
        fname, _ = QFileDialog.getOpenFileName(self, '打开', '', 'Images (*.png *.jpg *.jpeg *.bmp *.webp)')
        if fname:
            self.original_image = Image.open(fname).convert("RGBA")
            self.update_image()
            self.view.fit_image()

    def update_image(self):
        if self.original_image is None: return
        
        vals = {n: s.value() for n, s in self.sliders.items()}
        for n, l in self.value_labels.items(): l.setText(str(vals[n]))

        img = self.original_image.copy()
        
        # 1. 亮度与对比度
        img = ImageEnhance.Brightness(img).enhance(vals["亮度"] / 100.0)
        img = ImageEnhance.Contrast(img).enhance(vals["对比度"] / 100.0)

        # 2. 灰度/饱和度处理
        sat_factor = vals["灰度/饱和度"] / 100.0
        if sat_factor != 1.0:
            if self.cb_protect_white.isChecked():
                # --- 修复后的掩码生成逻辑 ---
                r, g, b, a = img.split()
                threshold = 240
                # 对每个通道生成 0/255 的阈值图
                mask_r = r.point(lambda p: 255 if p > threshold else 0)
                mask_g = g.point(lambda p: 255 if p > threshold else 0)
                mask_b = b.point(lambda p: 255 if p > threshold else 0)
                # 使用 ImageChops.lighter/darker 做交集运算（R>240 且 G>240 且 B>240）
                white_mask = ImageChops.darker(mask_r, mask_g)
                white_mask = ImageChops.darker(white_mask, mask_b)
                
                full_processed = ImageEnhance.Color(img).enhance(sat_factor)
                # 合成：white_mask 为 255 的地方用 img (原色)，0 的地方用 full_processed (灰度)
                img = Image.composite(img, full_processed, white_mask)
            else:
                img = ImageEnhance.Color(img).enhance(sat_factor)

        # 3. 色相旋转
        if vals["色相旋转"] != 0:
            r, g, b, a = img.split()
            rgb = Image.merge('RGB', (r, g, b)).convert('HSV')
            h, s, v = rgb.split()
            h = h.point(lambda p: (p + int(vals["色相旋转"] * 255 / 360)) % 256)
            rgb = Image.merge('HSV', (h, s, v)).convert('RGB')
            img = Image.merge('RGBA', (*rgb.split(), a))

        # 4. 透明度
        alpha_val = int(vals["不透明度"] * 2.55)
        r, g, b, a = img.split()
        a = a.point(lambda p: min(p, alpha_val))
        img = Image.merge('RGBA', (r, g, b, a))

        self.processed_image = img
        self.display_image(img)

    def display_image(self, pil_img):
        try:
            data = pil_img.tobytes("raw", "RGBA")
            qim = QImage(data, pil_img.size[0], pil_img.size[1], QImage.Format_RGBA8888)
            qim.data = data 
            self.view.set_image(QPixmap.fromImage(qim))
        except Exception as e:
            print(f"Error: {e}")

    def save_image(self):
        if self.processed_image:
            fname, _ = QFileDialog.getSaveFileName(self, '导出', 'result.png', 'PNG (*.png);;JPG (*.jpg)')
            if fname:
                out = self.processed_image
                if fname.lower().endswith(('.jpg', '.jpeg')): out = out.convert("RGB")
                out.save(fname)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernImageEditor()
    window.show()
    sys.exit(app.exec_())