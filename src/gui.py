"""
GUI Module for PyPass - Offline Password Generator
Tkinter-based user interface with modern styling and accessibility features
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import time
import re
from datetime import datetime
from .password_generator import SecurePasswordGenerator, PersonalInfo, PasswordOptions


class ClipboardManager:
    """Manages clipboard operations with auto-clear functionality"""

    def __init__(self, root):
        self.root = root
        self.clear_timer = None

    def copy_to_clipboard(self, text: str):
        """Copy text to clipboard and start auto-clear timer"""
        self.root.clipboard_clear()
        self.root.clipboard_append(text)

        # Cancel existing timer if any
        if self.clear_timer:
            self.clear_timer.cancel()

        # Start new timer for 30 seconds
        self.clear_timer = threading.Timer(30.0, self._clear_clipboard)
        self.clear_timer.start()

    def _clear_clipboard(self):
        """Clear clipboard contents"""
        try:
            self.root.clipboard_clear()
        except (tk.TclError, RuntimeError):
            pass  # Handle case where app is closed or main thread not in main loop


class PasswordGeneratorApp:
    """Main application class for PyPass GUI"""

    def __init__(self):
        self.root = tk.Tk()
        self.password_generator = SecurePasswordGenerator()
        self.clipboard_manager = ClipboardManager(self.root)
        self.current_password = ""
        self.password_visible = False

        self._setup_window()
        self._create_widgets()
        self._setup_layout()
        self._setup_bindings()

    def _setup_window(self):
        """Configure main window properties"""
        self.root.title("PyPass - Offline Password Generator")
        self.root.geometry("600x800")
        self.root.resizable(True, True)

        # Set minimum size
        self.root.minsize(500, 700)

        # Configure window icon (would need an icon file)
        try:
            # self.root.iconbitmap('icon.ico')  # Uncomment if you have an icon
            pass
        except:
            pass

        # Configure style
        style = ttk.Style()
        style.theme_use('clam')  # Modern looking theme

    def _create_widgets(self):
        """Create all GUI widgets"""
        # Main container
        self.main_frame = ttk.Frame(self.root, padding="20")

        # Title
        self.title_label = ttk.Label(
            self.main_frame,
            text="PyPass - Secure Password Generator",
            font=("Segoe UI", 16, "bold")
        )

        # Personal Information Section
        self.info_frame = ttk.LabelFrame(
            self.main_frame, text="Personal Information", padding="10")

        # Input fields
        self.first_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.birth_date_var = tk.StringVar()
        self.current_date_var = tk.StringVar(
            value=datetime.now().strftime("%d-%m-%Y"))
        self.platform_var = tk.StringVar()
        self.city_var = tk.StringVar()

        # Create input widgets
        self._create_input_widgets()

        # Password Options Section
        self.options_frame = ttk.LabelFrame(
            self.main_frame, text="Password Options", padding="10")

        # Password length
        self.length_var = tk.IntVar(value=12)
        self.length_label = ttk.Label(
            self.options_frame, text="Password Length:")
        self.length_scale = ttk.Scale(
            self.options_frame,
            from_=8, to=20,
            variable=self.length_var,
            orient="horizontal"
        )
        self.length_value_label = ttk.Label(self.options_frame, text="12")

        # Character type checkboxes
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)
        self.exclude_ambiguous = tk.BooleanVar(value=True)

        self._create_option_widgets()

        # Password Output Section
        self.output_frame = ttk.LabelFrame(
            self.main_frame, text="Generated Password", padding="10")

        # Password display
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(
            self.output_frame,
            textvariable=self.password_var,
            show="*",
            state="readonly",
            font=("Consolas", 12)
        )

        # Password strength
        self.strength_label = ttk.Label(
            self.output_frame, text="Strength: Not Generated")
        self.strength_progress = ttk.Progressbar(
            self.output_frame,
            length=200,
            mode='determinate'
        )

        # Buttons
        self._create_button_widgets()

    def _create_input_widgets(self):
        """Create personal information input widgets"""
        # First Name
        ttk.Label(self.info_frame, text="First Name:").grid(
            row=0, column=0, sticky="w", pady=2)
        self.first_name_entry = ttk.Entry(
            self.info_frame, textvariable=self.first_name_var, width=30)
        self.first_name_entry.grid(row=0, column=1, pady=2, padx=(10, 0))

        # Last Name
        ttk.Label(self.info_frame, text="Last Name:").grid(
            row=1, column=0, sticky="w", pady=2)
        self.last_name_entry = ttk.Entry(
            self.info_frame, textvariable=self.last_name_var, width=30)
        self.last_name_entry.grid(row=1, column=1, pady=2, padx=(10, 0))

        # Date of Birth
        ttk.Label(self.info_frame, text="Date of Birth (dd-mm-yyyy):").grid(row=2,
                                                                            column=0, sticky="w", pady=2)
        self.birth_date_entry = ttk.Entry(
            self.info_frame, textvariable=self.birth_date_var, width=30)
        self.birth_date_entry.grid(row=2, column=1, pady=2, padx=(10, 0))

        # Current Date
        ttk.Label(self.info_frame, text="Current Date:").grid(
            row=3, column=0, sticky="w", pady=2)
        self.current_date_entry = ttk.Entry(
            self.info_frame, textvariable=self.current_date_var, width=30)
        self.current_date_entry.grid(row=3, column=1, pady=2, padx=(10, 0))

        # Platform
        ttk.Label(self.info_frame, text="Platform/Service:").grid(row=4,
                                                                  column=0, sticky="w", pady=2)
        self.platform_entry = ttk.Entry(
            self.info_frame, textvariable=self.platform_var, width=30)
        self.platform_entry.grid(row=4, column=1, pady=2, padx=(10, 0))

        # City
        ttk.Label(self.info_frame, text="Current City:").grid(
            row=5, column=0, sticky="w", pady=2)
        self.city_entry = ttk.Entry(
            self.info_frame, textvariable=self.city_var, width=30)
        self.city_entry.grid(row=5, column=1, pady=2, padx=(10, 0))

        # Add tooltips (simple implementation)
        self._add_tooltip(self.birth_date_entry, "Format: 25-12-1990")

    def _create_option_widgets(self):
        """Create password option widgets"""
        # Length controls
        self.length_label.grid(row=0, column=0, sticky="w", pady=5)
        self.length_scale.grid(
            row=0, column=1, sticky="ew", pady=5, padx=(10, 5))
        self.length_value_label.grid(row=0, column=2, pady=5)

        # Character type checkboxes
        ttk.Checkbutton(self.options_frame, text="Include Uppercase (A-Z)",
                        variable=self.include_uppercase).grid(row=1, column=0, columnspan=3, sticky="w", pady=2)
        ttk.Checkbutton(self.options_frame, text="Include Lowercase (a-z)",
                        variable=self.include_lowercase).grid(row=2, column=0, columnspan=3, sticky="w", pady=2)
        ttk.Checkbutton(self.options_frame, text="Include Numbers (0-9)",
                        variable=self.include_numbers).grid(row=3, column=0, columnspan=3, sticky="w", pady=2)
        ttk.Checkbutton(self.options_frame, text="Include Special Characters (!@#$...)",
                        variable=self.include_special).grid(row=4, column=0, columnspan=3, sticky="w", pady=2)
        ttk.Checkbutton(self.options_frame, text="Exclude Ambiguous Characters (0, O, l, I, 1)",
                        variable=self.exclude_ambiguous).grid(row=5, column=0, columnspan=3, sticky="w", pady=2)

        # Configure column weights
        self.options_frame.columnconfigure(1, weight=1)

    def _create_button_widgets(self):
        """Create button widgets"""
        # Button frame
        self.button_frame = ttk.Frame(self.output_frame)

        # Generate button
        self.generate_button = ttk.Button(
            self.button_frame,
            text="Generate Password",
            command=self.generate_password,
            style="Accent.TButton"
        )

        # Show/Hide button
        self.toggle_button = ttk.Button(
            self.button_frame,
            text="Show",
            command=self.toggle_password_visibility
        )

        # Copy button
        self.copy_button = ttk.Button(
            self.button_frame,
            text="Copy to Clipboard",
            command=self.copy_password
        )

        # Save button
        self.save_button = ttk.Button(
            self.button_frame,
            text="Save to File",
            command=self.save_password
        )

        # Clear button
        self.clear_button = ttk.Button(
            self.button_frame,
            text="Clear All",
            command=self.clear_all
        )

    def _setup_layout(self):
        """Setup widget layout using grid geometry manager"""
        # Main frame
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Configure root grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Configure main frame grid weights
        self.main_frame.columnconfigure(0, weight=1)

        # Title
        self.title_label.grid(row=0, column=0, pady=(0, 20))

        # Personal info section
        self.info_frame.grid(row=1, column=0, sticky="ew", pady=(0, 15))
        self.info_frame.columnconfigure(1, weight=1)

        # Options section
        self.options_frame.grid(row=2, column=0, sticky="ew", pady=(0, 15))

        # Output section
        self.output_frame.grid(row=3, column=0, sticky="ew", pady=(0, 15))
        self.output_frame.columnconfigure(0, weight=1)

        # Password entry
        self.password_entry.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        # Strength indicators
        self.strength_label.grid(row=1, column=0, sticky="w", pady=(0, 5))
        self.strength_progress.grid(row=2, column=0, sticky="ew", pady=(0, 15))

        # Button frame
        self.button_frame.grid(row=3, column=0, sticky="ew")
        self.button_frame.columnconfigure((0, 1, 2, 3, 4), weight=1)

        # Buttons
        self.generate_button.grid(row=0, column=0, padx=2, pady=2, sticky="ew")
        self.toggle_button.grid(row=0, column=1, padx=2, pady=2, sticky="ew")
        self.copy_button.grid(row=0, column=2, padx=2, pady=2, sticky="ew")
        self.save_button.grid(row=0, column=3, padx=2, pady=2, sticky="ew")
        self.clear_button.grid(row=0, column=4, padx=2, pady=2, sticky="ew")

    def _setup_bindings(self):
        """Setup event bindings"""
        # Length scale update
        self.length_scale.configure(command=self._update_length_label)

        # Entry field validation bindings could be added here

        # Window close event
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _update_length_label(self, value):
        """Update length label when scale changes"""
        self.length_value_label.config(text=str(int(float(value))))

    def _add_tooltip(self, widget, text):
        """Simple tooltip implementation"""
        def on_enter(event):
            # Create tooltip window
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.configure(bg="lightyellow")

            # Position tooltip
            x = event.widget.winfo_rootx() + 20
            y = event.widget.winfo_rooty() - 30
            tooltip.wm_geometry(f"+{x}+{y}")

            # Add text
            label = tk.Label(tooltip, text=text, bg="lightyellow",
                             relief="solid", borderwidth=1)
            label.pack()

            # Store reference
            widget.tooltip = tooltip

        def on_leave(event):
            if hasattr(event.widget, 'tooltip'):
                event.widget.tooltip.destroy()
                del event.widget.tooltip

        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

    def _validate_inputs(self) -> bool:
        """Validate user inputs"""
        # Check if all fields are filled
        if not all([
            self.first_name_var.get().strip(),
            self.last_name_var.get().strip(),
            self.birth_date_var.get().strip(),
            self.current_date_var.get().strip(),
            self.platform_var.get().strip(),
            self.city_var.get().strip()
        ]):
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return False

        # Validate date format
        date_pattern = r'^\d{2}-\d{2}-\d{4}$'

        if not re.match(date_pattern, self.birth_date_var.get()):
            messagebox.showerror(
                "Date Error", "Birth date must be in dd-mm-yyyy format.")
            return False

        if not re.match(date_pattern, self.current_date_var.get()):
            messagebox.showerror(
                "Date Error", "Current date must be in dd-mm-yyyy format.")
            return False

        # Check if at least one character type is selected
        if not any([
            self.include_uppercase.get(),
            self.include_lowercase.get(),
            self.include_numbers.get(),
            self.include_special.get()
        ]):
            messagebox.showerror(
                "Options Error", "Please select at least one character type.")
            return False

        return True

    def generate_password(self):
        """Generate a new password"""
        if not self._validate_inputs():
            return

        try:
            # Create personal info object
            personal_info = PersonalInfo(
                first_name=self.first_name_var.get(),
                last_name=self.last_name_var.get(),
                birth_date=self.birth_date_var.get(),
                current_date=self.current_date_var.get(),
                platform=self.platform_var.get(),
                city=self.city_var.get()
            )

            # Create options object
            options = PasswordOptions()
            options.length = self.length_var.get()
            options.include_uppercase = self.include_uppercase.get()
            options.include_lowercase = self.include_lowercase.get()
            options.include_numbers = self.include_numbers.get()
            options.include_special = self.include_special.get()
            options.exclude_ambiguous = self.exclude_ambiguous.get()

            # Set generator configuration
            self.password_generator.set_personal_info(personal_info)
            self.password_generator.set_options(options)

            # Generate password
            self.current_password = self.password_generator.generate_password()

            # Update display
            self.password_var.set(self.current_password)
            if self.password_visible:
                self.password_entry.config(show="")
                self.toggle_button.config(text="Hide")
            else:
                self.password_entry.config(show="*")
                self.toggle_button.config(text="Show")

            # Update strength indicator
            strength_label, strength_score = self.password_generator.assess_strength(
                self.current_password)
            self.strength_label.config(
                text=f"Strength: {strength_label} ({strength_score:.1f}%)")
            self.strength_progress.config(value=strength_score)

            # Update button states
            self.toggle_button.config(state="normal")
            self.copy_button.config(state="normal")
            self.save_button.config(state="normal")

        except Exception as e:
            messagebox.showerror("Generation Error",
                                 f"Failed to generate password: {str(e)}")

    def toggle_password_visibility(self):
        """Toggle password visibility"""
        if not self.current_password:
            return

        self.password_visible = not self.password_visible

        if self.password_visible:
            self.password_entry.config(show="")
            self.toggle_button.config(text="Hide")
        else:
            self.password_entry.config(show="*")
            self.toggle_button.config(text="Show")

    def copy_password(self):
        """Copy password to clipboard"""
        if not self.current_password:
            messagebox.showwarning(
                "No Password", "Please generate a password first.")
            return

        self.clipboard_manager.copy_to_clipboard(self.current_password)
        messagebox.showinfo(
            "Copied", "Password copied to clipboard.\nIt will be cleared automatically in 30 seconds.")

    def save_password(self):
        """Save password to file"""
        if not self.current_password:
            messagebox.showwarning(
                "No Password", "Please generate a password first.")
            return

        # Generate filename
        platform = self.platform_var.get().replace(" ", "_").replace("/", "_")
        filename = f"{platform}_password.txt"

        # Open file dialog
        file_path = filedialog.asksaveasfilename(
            initialfile=filename,
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )

        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(f"Password for {self.platform_var.get()}\n")
                    f.write(
                        f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write(f"Password: {self.current_password}\n")
                    f.write(
                        "\nNote: Keep this file secure and delete when no longer needed.\n")

                messagebox.showinfo(
                    "Saved", f"Password saved to:\n{file_path}")
            except Exception as e:
                messagebox.showerror(
                    "Save Error", f"Failed to save password: {str(e)}")

    def clear_all(self):
        """Clear all fields and generated password"""
        # Clear input fields
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.birth_date_var.set("")
        self.current_date_var.set(datetime.now().strftime("%d-%m-%Y"))
        self.platform_var.set("")
        self.city_var.set("")

        # Reset options to defaults
        self.length_var.set(12)
        self.include_uppercase.set(True)
        self.include_lowercase.set(True)
        self.include_numbers.set(True)
        self.include_special.set(True)
        self.exclude_ambiguous.set(True)

        # Clear password
        self.current_password = ""
        self.password_var.set("")
        self.password_visible = False
        self.password_entry.config(show="*")

        # Reset strength indicator
        self.strength_label.config(text="Strength: Not Generated")
        self.strength_progress.config(value=0)

        # Reset button states
        self.toggle_button.config(text="Show", state="disabled")
        self.copy_button.config(state="disabled")
        self.save_button.config(state="disabled")

        # Update length label
        self.length_value_label.config(text="12")

    def _on_closing(self):
        """Handle window closing event"""
        # Clear clipboard if timer is running
        if self.clipboard_manager.clear_timer:
            self.clipboard_manager.clear_timer.cancel()
            self.clipboard_manager._clear_clipboard()

        self.root.destroy()

    def run(self):
        """Start the application"""
        # Initialize button states
        self.toggle_button.config(state="disabled")
        self.copy_button.config(state="disabled")
        self.save_button.config(state="disabled")
        self.password_entry.config(show="*")

        # Start main loop
        self.root.mainloop()


if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.run()
