import tkinter as tk
from app.services.vendor_service import VendorService

class VendorApp:
    def __init__(self, root):
        self.root = root
        self.vendor_service = VendorService()
        self.create_widgets()

    def create_widgets(self):
        # 标题
        self.title_label = tk.Label(self.root, text="Vendor Management")
        self.title_label.pack()

        # 列表框
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack()
        self.list_label = tk.Label(self.list_frame, text="Vendor List:")
        self.list_label.pack()
        self.list_text = tk.Text(self.list_frame, width=80, height=10)
        self.list_text.pack()

        # 添加按钮
        self.add_button = tk.Button(self.root, text="Add Vendor", command=self.add_vendor)
        self.add_button.pack()

        # 退出按钮
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.pack()

        # 刷新列表
        self.refresh_list()

    def refresh_list(self):
        self.list_text.delete(1.0, tk.END)
        vendors = self.vendor_service.get_all_vendors()
        for vendor in vendors:
            self.list_text.insert(tk.END, f"ID: {vendor['vendor_id']}, Business Name: {vendor['business_name']}, "
                                          f"Feedback Score: {vendor['customer_feedback_score']}, "
                                          f"Geographical Presence: {vendor['geographical_presence']}\n")

    def add_vendor(self):
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Add Vendor")

        # 商业名称
        self.business_name_label = tk.Label(self.add_window, text="Business Name:")
        self.business_name_label.pack()
        self.business_name_entry = tk.Entry(self.add_window, width=50)
        self.business_name_entry.pack()

        # 客户反馈评分
        self.customer_feedback_score_label = tk.Label(self.add_window, text="Customer Feedback Score:")
        self.customer_feedback_score_label.pack()
        self.customer_feedback_score_entry = tk.Entry(self.add_window, width=50)
        self.customer_feedback_score_entry.pack()

        # 地理位置
        self.geographical_presence_label = tk.Label(self.add_window, text="Geographical Presence:")
        self.geographical_presence_label.pack()
        self.geographical_presence_entry = tk.Entry(self.add_window, width=50)
        self.geographical_presence_entry.pack()

        # 添加按钮
        self.add_button = tk.Button(self.add_window, text="Add", command=self.add_vendor_confirm)
        self.add_button.pack()

    def add_vendor_confirm(self):
        business_name = self.business_name_entry.get()
        customer_feedback_score = self.customer_feedback_score_entry.get()
        if customer_feedback_score:
            customer_feedback_score = float(customer_feedback_score)
        else:
            customer_feedback_score = None
        geographical_presence = self.geographical_presence_entry.get()
        if not geographical_presence:
            geographical_presence = None
        self.vendor_service.create_vendor(business_name, customer_feedback_score, geographical_presence)
        self.refresh_list()
        self.add_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = VendorApp(root)
    root.mainloop()
