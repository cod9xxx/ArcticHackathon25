template_quiz = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>977</width>
    <height>717</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">
QRadioButton {
    font-family: &quot;Segoe UI&quot;, &quot;Roboto&quot;, &quot;Arial&quot;;
    font-size: 12pt;
    color: #1a1a1a;

}


QRadioButton::indicator {
    width: 12px;
    height: 12px;
    border-radius: 7px;
border: 2px solid #888;
    background: white;
}

QRadioButton::indicator:hover {
    border-color: #5aaaff;
}

QRadioButton::indicator:pressed {
    background: #dceeff;
}


QRadioButton::indicator:checked {
    border: 2px solid #2a7cff;
    background: #2a7cff;
}

</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>380</x>
     <y>10</y>
     <width>201</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">
    color: #1560BD;
    border-radius: 12px;
    padding: 10px 20px;
    font-size: 48px;
    font-family: &quot;Segoe UI&quot;, &quot;Roboto&quot;, sans-serif;</string>
   </property>
   <property name="text">
    <string>КВИЗ</string>
   </property>
  </widget>
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>80</y>
     <width>941</width>
     <height>551</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QLabel" name="label_3">
      <property name="maximumSize">
       <size>
        <width>2000</width>
        <height>16777215</height>
       </size>
      </property>
      <property name="styleSheet">
       <string notr="true">  font-size: 14pt;</string>
      </property>
      <property name="text">
       <string>1. Какая исследовательская база является российской и расположена глубоко в Антарктиде?</string>
      </property>
     </widget>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout">
      <item>
       <widget class="QRadioButton" name="answer1_1">
        <property name="sizePolicy">
         <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
          <horstretch>0</horstretch>
          <verstretch>0</verstretch>
         </sizepolicy>
        </property>
        <property name="text">
         <string>Мак-Мердо</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QRadioButton" name="answer1_2">
        <property name="text">
         <string> Амундсен–Скотт</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QRadioButton" name="answer1_3">
        <property name="text">
         <string>Восток</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QRadioButton" name="answer1_4">
        <property name="text">
         <string>Моусон</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item>
     <widget class="QLabel" name="label_4">
      <property name="styleSheet">
       <string notr="true">  font-size: 14pt;</string>
      </property>
      <property name="text">
       <string>2. Какое животное из базы данных имеет клыки длиной до метра и питается моллюсками?</string>
      </property>
     </widget>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_2">
      <item>
       <widget class="QRadioButton" name="answer2_1">
        <property name="text">
         <string>Мускусный бык</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QRadioButton" name="answer2_2">
        <property name="text">
         <string>Северный олень</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QRadioButton" name="answer2_3">
        <property name="text">
         <string> Морж</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QRadioButton" name="answer2_4">
        <property name="text">
         <string>Пингвин</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item>
     <widget class="QLabel" name="label_5">
      <property name="styleSheet">
       <string notr="true">  font-size: 14pt;</string>
      </property>
      <property name="text">
       <string>3. Какая станция расположена на географическом Южном полюсе?</string>
      </property>
     </widget>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_3">
      <item>
       <widget class="QRadioButton" name="answer3_1">
        <property name="text">
         <string>Станция Мак-Мердо</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QRadioButton" name="answer3_2">
        <property name="text">
         <string>База Эсперанса</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QRadioButton" name="answer3_3">
        <property name="text">
         <string>Станция Восток</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QRadioButton" name="answer3_4">
        <property name="text">
         <string>Станция Амундсен-Скотт</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item>
     <widget class="QLabel" name="label_6">
      <property name="styleSheet">
       <string notr="true">  font-size: 14pt;</string>
      </property>
      <property name="text">
       <string>4.  Какое растение является единственным цветковым, растущим на Антарктическом полуострове?</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_4">
      <item>
       <widget class="QRadioButton" name="answer4_1">
        <property name="text">
         <string>Антарктический лишайник</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QRadioButton" name="answer4_2">
        <property name="text">
         <string>Антарктическая жемчужина</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QRadioButton" name="answer4_3">
        <property name="text">
         <string> Псевдотреугольный бриум</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QRadioButton" name="answer4_4">
        <property name="text">
         <string> Антарктический мох</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item>
     <widget class="QLabel" name="label_2">
      <property name="styleSheet">
       <string notr="true">  font-size: 14pt;</string>
      </property>
      <property name="text">
       <string>5.  Какое животное покрыто густой шерстью и защищается, сбиваясь в стада?</string>
      </property>
     </widget>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_5">
      <item>
       <widget class="QRadioButton" name="answer5_1">
        <property name="sizePolicy">
         <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
          <horstretch>0</horstretch>
          <verstretch>0</verstretch>
         </sizepolicy>
        </property>
        <property name="text">
         <string>Пингвин</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QRadioButton" name="answer5_2">
        <property name="text">
         <string>Мускусный бык</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QRadioButton" name="answer5_3">
        <property name="text">
         <string>Морж</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QRadioButton" name="answer5_4">
        <property name="text">
         <string>Песец</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <widget class="QPushButton" name="end_btn">
   <property name="geometry">
    <rect>
     <x>340</x>
     <y>640</y>
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
    <string>ЗАВЕРШИТЬ</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""