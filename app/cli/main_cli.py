from app.services.vendor_service import VendorService


def main_cli():
    vendor_service = VendorService()
    while True:
        print("\n1. List all vendors")
        print("2. Add a new vendor")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            vendors = vendor_service.get_all_vendors()
            for vendor in vendors:
                print(f"ID: {vendor['vendor_id']}, Business Name: {vendor['business_name']}, "
                      f"Feedback Score: {vendor['customer_feedback_score']}, "
                      f"Geographical Presence: {vendor['geographical_presence']}")
        elif choice == '2':
            business_name = input("Enter vendor business name: ")
            customer_feedback_score = input("Enter customer feedback score (optional, press enter to skip): ")
            if customer_feedback_score:
                customer_feedback_score = float(customer_feedback_score)
            else:
                customer_feedback_score = None
            geographical_presence = input("Enter geographical presence (optional, press enter to skip): ")
            if not geographical_presence:
                geographical_presence = None
            vendor_service.create_vendor(business_name, customer_feedback_score, geographical_presence)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")