template_station ="""<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>661</width>
    <height>536</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QLabel" name="stationPhoto_label">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>70</y>
     <width>331</width>
     <height>301</height>
    </rect>
   </property>
   <property name="text">
    <string>ФОТО</string>
   </property>
  </widget>
  <widget class="QFrame" name="frame">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>390</y>
     <width>631</width>
     <height>131</height>
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
   <widget class="QLabel" name="stationInfo_label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>611</width>
      <height>111</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: white;
    font-family: &quot;Segoe UI Light&quot;, &quot;Roboto Light&quot;, sans-serif;
    font-size: 18px;
    font-weight: 300;</string>
    </property>
    <property name="text">
     <string>ОПИСАНИЕ</string>
    </property>
   </widget>
  </widget>
  <widget class="QLabel" name="stationName_label">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>20</y>
     <width>511</width>
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
    <string>НАЗВАНИЕ СТАНЦИИ</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>370</x>
     <y>70</y>
     <width>131</width>
     <height>311</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QLabel" name="label_2">
      <property name="styleSheet">
       <string notr="true">
    color: #4682B4;
    font-family: &quot;Segoe UI Semibold&quot;, &quot;Roboto Medium&quot;, sans-serif;
    font-size: 16px;
    font-weight: 600;</string>
      </property>
      <property name="text">
       <string>Температура:</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="label">
      <property name="styleSheet">
       <string notr="true">
    color: #4682B4;
    font-family: &quot;Segoe UI Semibold&quot;, &quot;Roboto Medium&quot;, sans-serif;
    font-size: 16px;
    font-weight: 600;</string>
      </property>
      <property name="text">
       <string>Скорость ветра:</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="label_3">
      <property name="styleSheet">
       <string notr="true">
    color: #4682B4;
    font-family: &quot;Segoe UI Semibold&quot;, &quot;Roboto Medium&quot;, sans-serif;
    font-size: 16px;
    font-weight: 600;</string>
      </property>
      <property name="text">
       <string>Влажность:</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="label_4">
      <property name="styleSheet">
       <string notr="true">
    color: #4682B4;
    font-family: &quot;Segoe UI Semibold&quot;, &quot;Roboto Medium&quot;, sans-serif;
    font-size: 16px;
    font-weight: 600;</string>
      </property>
      <property name="text">
       <string>Давление:</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="label_5">
      <property name="styleSheet">
       <string notr="true">
    color: #4682B4;
    font-family: &quot;Segoe UI Semibold&quot;, &quot;Roboto Medium&quot;, sans-serif;
    font-size: 16px;
    font-weight: 600;</string>
      </property>
      <property name="text">
       <string>Погода:</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QWidget" name="verticalLayoutWidget_2">
   <property name="geometry">
    <rect>
     <x>510</x>
     <y>70</y>
     <width>141</width>
     <height>311</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout_2">
    <item>
     <widget class="QLabel" name="temperature_label">
      <property name="styleSheet">
       <string notr="true">
    color: #4682B4;
    font-family: &quot;Segoe UI Semibold&quot;, &quot;Roboto Medium&quot;, sans-serif;
    font-size: 16px;
    font-weight: 600;</string>
      </property>
      <property name="text">
       <string>1</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="wind_label">
      <property name="styleSheet">
       <string notr="true">
    color: #4682B4;
    font-family: &quot;Segoe UI Semibold&quot;, &quot;Roboto Medium&quot;, sans-serif;
    font-size: 16px;
    font-weight: 600;</string>
      </property>
      <property name="text">
       <string>2</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="humidity_label">
      <property name="styleSheet">
       <string notr="true">
    color: #4682B4;
    font-family: &quot;Segoe UI Semibold&quot;, &quot;Roboto Medium&quot;, sans-serif;
    font-size: 16px;
    font-weight: 600;</string>
      </property>
      <property name="text">
       <string>3</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="pressure_label">
      <property name="styleSheet">
       <string notr="true">
    color: #4682B4;
    font-family: &quot;Segoe UI Semibold&quot;, &quot;Roboto Medium&quot;, sans-serif;
    font-size: 16px;
    font-weight: 600;</string>
      </property>
      <property name="text">
       <string>4</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="condition_label">
      <property name="styleSheet">
       <string notr="true">
    color: #4682B4;
    font-family: &quot;Segoe UI Semibold&quot;, &quot;Roboto Medium&quot;, sans-serif;
    font-size: 16px;
    font-weight: 600;</string>
      </property>
      <property name="text">
       <string>5</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""