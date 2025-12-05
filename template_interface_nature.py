template_nature = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>740</width>
    <height>438</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QLabel" name="photo_label">
   <property name="geometry">
    <rect>
     <x>40</x>
     <y>80</y>
     <width>311</width>
     <height>331</height>
    </rect>
   </property>
   <property name="text">
    <string>ФОТО</string>
   </property>
  </widget>
  <widget class="QFrame" name="frame">
   <property name="geometry">
    <rect>
     <x>360</x>
     <y>80</y>
     <width>351</width>
     <height>331</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color:  #42AAFF;
    border-radius: 8px;
    border: 1px solid #4DA8FF;
    margin: 4px;</string>
   </property>
   <property name="frameShape">
    <enum>QFrame::StyledPanel</enum>
   </property>
   <property name="frameShadow">
    <enum>QFrame::Raised</enum>
   </property>
   <widget class="QLabel" name="info_label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>331</width>
      <height>311</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: white;
    font-family: &quot;Segoe UI Light&quot;, &quot;Roboto Light&quot;, sans-serif;
    font-size: 16px;
    font-weight: 300;</string>
    </property>
    <property name="text">
     <string>ОПИСАНИЕ</string>
    </property>
   </widget>
  </widget>
  <widget class="QLabel" name="name_label">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>20</y>
     <width>291</width>
     <height>41</height>
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
    <string>НАЗВАНИЕ</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""