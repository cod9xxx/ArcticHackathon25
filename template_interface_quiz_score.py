template_quiz_scores = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>521</width>
    <height>290</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">* {
    font-family: &quot;Poppins&quot;;
}

QMainWindow {
    background-color: #E6F7FF;
}


QLabel {
	color: #4682B4;
    font-size: 28px;
    background: transparent;
}

QPushButton {
    background-color: #4682B4;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 8px 14px;
    font-size: 16px;
}

QPushButton:hover {
    background-color: #3A6C95;
}

QPushButton:pressed {
    background-color: #2F5878;
}</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>0</y>
     <width>271</width>
     <height>71</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 32px</string>
   </property>
   <property name="text">
    <string>ВАШ РЕЗУЛЬТАТ:</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_3">
   <property name="geometry">
    <rect>
     <x>230</x>
     <y>70</y>
     <width>91</width>
     <height>101</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 100px</string>
   </property>
   <property name="text">
    <string>/5</string>
   </property>
  </widget>
  <widget class="QPushButton" name="again_btn">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>210</y>
     <width>251</width>
     <height>60</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">QPushButton {
    background-color: #1560BD;
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
    font-size: 20px;
    font-family: &quot;Segoe UI&quot;, &quot;Roboto&quot;, sans-serif;
    font-weight: 500;
    border: none;
    min-height: 40px;
    min-width: 80px;
}

QPushButton:hover {
    background-color: #1E7AE9;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #1E7AE9, stop:1 #1560BD);
}

QPushButton:pressed {
    background-color: #0F4A8D;
    padding-top: 11px;
    padding-bottom: 9px;
}</string>
   </property>
   <property name="text">
    <string>Попробовать снова</string>
   </property>
  </widget>
  <widget class="QPushButton" name="back_btn">
   <property name="geometry">
    <rect>
     <x>280</x>
     <y>210</y>
     <width>221</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">QPushButton {
    background-color: #1560BD;
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
    font-size: 20px;
    font-family: &quot;Segoe UI&quot;, &quot;Roboto&quot;, sans-serif;
    font-weight: 500;
    border: none;
    min-height: 40px;
    min-width: 80px;
}

QPushButton:hover {
    background-color: #1E7AE9;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #1E7AE9, stop:1 #1560BD);
}

QPushButton:pressed {
    background-color: #0F4A8D;
    padding-top: 11px;
    padding-bottom: 9px;
}</string>
   </property>
   <property name="text">
    <string>Завершить</string>
   </property>
  </widget>
  <widget class="QLabel" name="score_label">
   <property name="geometry">
    <rect>
     <x>180</x>
     <y>70</y>
     <width>51</width>
     <height>101</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 100px</string>
   </property>
   <property name="text">
    <string>0</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""