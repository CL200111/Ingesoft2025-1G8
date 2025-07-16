#!/bin/bash

#use_cases=( ... )  # same list as above
# List of use cases (excluding CU06 which you said is already done)
use_cases=(
"CU01_register_book_screen"
"CU02_register_condition_screen"
"CU03_restore_book_screen"
"CU04_digitize_book_screen"
"CU05_classify_book_screen"
"CU07_query_book_history_screen"
"CU08_generate_report_screen"
"CU09_create_user_screen"
"CU10_edit_user_screen"
"CU11_deactivate_user_screen"
"CU12_modify_book_screen"
"CU13_deactivate_book_screen"
"CU14_notification_screen"
"CU15_physical_qa_screen"
"CU16_filter_books_by_state_screen"
"CU17_search_books_screen"
"CU18_search_users_screen"
"CU19_assign_task_screen"
"CU20_change_password_screen"
"CU21_restore_password_screen"
"CU22_query_book_screen"
"CU23_download_book_screen"
"CU24_digital_qa_screen"
"CU25_create_category_screen"
)

OUTPUT_DIR="."
mkdir -p "$OUTPUT_DIR"

for uc in "${use_cases[@]}"; do
    class_base="${uc#CU??_}"
    class_name="$(echo "$class_base" | sed -E 's/(^|_)([a-z])/\U\2/g')"
    py_file="$OUTPUT_DIR/${uc}.py"
    ui_import_name="Ui_${uc}"

    echo "Creating $py_file..."

    {
      echo "from PyQt5.QtWidgets import QWidget"
#     echo "from ui.screens.ui_${uc} import ${ui_import_name}"
      ui_class_name=$(echo "$uc" | sed -E 's/^CU[0-9]+_//')
      echo "from ui.screens.ui_${uc} import Ui_${ui_class_name}"
      echo ""
      echo "class ${class_name}(QWidget):"
      echo "    def __init__(self):"
      echo "        super().__init__()"
#     echo "        self.ui = ${ui_import_name}()"
      echo "        self.ui = Ui_${ui_class_name}()"
      echo "        self.ui.setupUi(self)"
      echo ""
      echo "        self.ui.saveButton.clicked.connect(self.save_entry)"
      echo ""
      echo "    def save_entry(self):"
      echo "        value = self.ui.titleInput.text()"
      echo "        print(f\"✅ Saving ${class_base//_/ }: {value}\")"
    } > "$py_file"
done

echo "✅ All CU screen Python files generated."
