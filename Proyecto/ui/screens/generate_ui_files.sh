#!/bin/bash

# Template content for UI files
generate_ui_content() {
  local class_name=$1
  cat <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>${class_name}</class>
 <widget class="QWidget" name="${class_name}">
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QLabel" name="label_heading">
     <property name="text">
      <string>📚 ${class_name//_/ } Screen</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QLineEdit" name="titleInput">
     <property name="placeholderText">
      <string>Enter text...</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QPushButton" name="saveButton">
     <property name="text">
      <string>➕ Confirm</string>
     </property>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
EOF
}

# List of all CU screen files
use_cases=(
"CU01_register_book_screen.py"
"CU02_register_condition_screen.py"
"CU03_restore_book_screen.py"
"CU04_digitize_book_screen.py"
"CU05_classify_book_screen.py"
"CU07_query_book_history_screen.py"
"CU08_generate_report_screen.py"
"CU09_create_user_screen.py"
"CU10_edit_user_screen.py"
"CU11_deactivate_user_screen.py"
"CU12_modify_book_screen.py"
"CU13_deactivate_book_screen.py"
"CU14_notification_screen.py"
"CU15_physical_qa_screen.py"
"CU16_filter_books_by_state_screen.py"
"CU17_search_books_screen.py"
"CU18_search_users_screen.py"
"CU19_assign_task_screen.py"
"CU20_change_password_screen.py"
"CU21_restore_password_screen.py"
"CU22_query_book_screen.py"
"CU23_download_book_screen.py"
"CU24_digital_qa_screen.py"
"CU25_create_category_screen.py"
)

# Output directory for UI files (adjust if needed)
output_dir="."

for file in "${use_cases[@]}"; do
  base_name="${file%.py}"
  class_name="${base_name#CU??_}"
  ui_file="${base_name}.ui"

  echo "Creating ${ui_file}..."
  generate_ui_content "$class_name" > "$output_dir/$ui_file"
done

echo "✅ Done generating .ui files."
