template_ways="""<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>285</width>
    <height>183</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QComboBox" name="ways_comboBox">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>60</y>
     <width>261</width>
     <height>31</height>
    </rect>
   </property>
   <item>
    <property name="text">
     <string>-</string>
    </property>
   </item>
   <item>
    <property name="text">
     <string>Маршрут Джеймса Кука</string>
    </property>
   </item>
   <item>
    <property name="text">
     <string>Маршрут Беллинсгаузена и Лазарева</string>
    </property>
   </item>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>-10</x>
     <y>10</y>
     <width>231</width>
     <height>51</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">
    color: #1560BD;
    border-radius: 12px;
    padding: 10px 20px;
    font-size: 20px;
    font-family: &quot;Segoe UI&quot;, &quot;Roboto&quot;, sans-serif;


</string>
   </property>
   <property name="text">
    <string>Выберите маршрут:</string>
   </property>
  </widget>
  <widget class="QPushButton" name="save_btn">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>110</y>
     <width>261</width>
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
    <string>Сохранить</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""