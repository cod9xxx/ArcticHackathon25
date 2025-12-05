template_fact = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>632</width>
    <height>465</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>20</y>
     <width>401</width>
     <height>51</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">
    color: #4682B4;
    font-family: &quot;Segoe UI Semibold&quot;, &quot;Roboto Medium&quot;, sans-serif;
    font-size: 32px;
    font-weight: 600;</string>
   </property>
   <property name="text">
    <string>ИНТЕРЕСНЫЕ ФАКТЫ</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>50</x>
     <y>100</y>
     <width>51</width>
     <height>261</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QLabel" name="label_2">
      <property name="styleSheet">
       <string notr="true">
    color: #1560BD;

    font-size: 22px;

</string>
      </property>
      <property name="text">
       <string>1</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignCenter</set>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="label_3">
      <property name="styleSheet">
       <string notr="true">
    color: #1560BD;

    font-size: 22px;

</string>
      </property>
      <property name="text">
       <string>2</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignCenter</set>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="label_4">
      <property name="styleSheet">
       <string notr="true">
    color: #1560BD;

    font-size: 22px;

</string>
      </property>
      <property name="text">
       <string>3</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignCenter</set>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QLabel" name="first_fact">
   <property name="geometry">
    <rect>
     <x>100</x>
     <y>100</y>
     <width>491</width>
     <height>81</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">
    color: #1560BD;

    font-size: 16px;

</string>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="wordWrap">
    <bool>true</bool>
   </property>
  </widget>
  <widget class="QLabel" name="third_fact">
   <property name="geometry">
    <rect>
     <x>100</x>
     <y>280</y>
     <width>491</width>
     <height>81</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">
    color: #1560BD;

    font-size: 16px;

</string>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="wordWrap">
    <bool>true</bool>
   </property>
  </widget>
  <widget class="QLabel" name="second_fact">
   <property name="geometry">
    <rect>
     <x>100</x>
     <y>190</y>
     <width>491</width>
     <height>81</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">
    color: #1560BD;

    font-size: 16px;

</string>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="wordWrap">
    <bool>true</bool>
   </property>
  </widget>
  <widget class="QPushButton" name="generate_button">
   <property name="geometry">
    <rect>
     <x>200</x>
     <y>380</y>
     <width>241</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">QPushButton {
    background-color: #1560BD;
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
    font-size: 24px;
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
    <string>СГЕНЕРИРОВАТЬ</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>'''
