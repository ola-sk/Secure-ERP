from model import util
from model.crm import crm
from model.crm.crm import CUSTOMER_DATAFILE, CUSTOMER_TABLE_HEADERS, CUSTOMER_TABLE_INDEXES, SUBSCRIPTION_STATUSES, \
    ALTERNATIVES
from view import terminal as view
from verify_email import verify_email
from controller import helpers


def list_customers():
    customer_table = crm.read_customer_data(CUSTOMER_DATAFILE, CUSTOMER_TABLE_HEADERS)
    if customer_table is not None:
        view.print_table(customer_table)
    else:
        view.print_error_message("Customer data couldn't be accessed.")


def add_customer(yes: list, no: list) -> bool:
    is_success = None
    try:
        customer_table = crm.read_customer_data(CUSTOMER_DATAFILE)
        customer_ids_taken = crm.get_customer_ids(customer_table)
        if customer_ids_taken is None:
            raise ValueError("Couldn't fetch customer ids. This step is necessary to generate a unique ID for a new "
                             "customer.")
        new_customer_id = util.generate_unique_id(customer_ids_taken)
        new_customers_data = []
        for header in CUSTOMER_TABLE_HEADERS:
            if header.lower() == "id" and len(new_customers_data) == 0:
                new_customers_data.append(new_customer_id)
            elif header.lower() == "id" and len(new_customers_data) != 0:
                raise ValueError("The new customer data at the time of writing is intended to be empty before filling "
                                 "out.")
            elif header.lower() == "name":
                name = view.get_input(header)
                new_customers_data.append(name)
            elif header.lower() == "email":
                is_correct_email_entered = False
                while not is_correct_email_entered:
                    email = view.get_input(header)
                    if verify_email(email):
                        new_customers_data.append(email)
                        is_correct_email_entered = True
                    else:
                        view.print_error_message("The e-mail address could not be verified. Please try entering it "
                                                 "again.")
            elif header.lower() == "subscribed":
                is_correct_subscription_status_entered = False
                while not is_correct_subscription_status_entered:
                    get_subscription_status = view.get_input("Is subscribed to the newsletter? "
                                                             "yes('yes', 'tak', 'y', '1')/ "
                                                             "no('no', 'nie', 'n', '0')")
                    is_subscription_status_valid = helpers.validate_input(get_subscription_status, yes + no)
                    if is_subscription_status_valid:
                        is_subscribed = None
                        try:
                            if helpers.validate_input(get_subscription_status, yes):
                                is_subscribed = SUBSCRIPTION_STATUSES["subscribed"]
                                is_correct_subscription_status_entered = True
                            elif helpers.validate_input(get_subscription_status, no):
                                is_subscribed = SUBSCRIPTION_STATUSES["not subscribed"]
                                is_correct_subscription_status_entered = True
                            else:
                                raise ValueError("Second validation of subscription status failed.")
                        except ValueError as error:
                            view.print_error_message(error)
                            continue
                        if is_subscribed is not None:
                            new_customers_data.append(is_subscribed)
                        else:
                            raise TypeError("Expected the subscription status, but got None. "
                                            "Program failed at parsing the subscription status input.")
        if helpers.is_number_of_fields_valid(new_customers_data, CUSTOMER_TABLE_HEADERS):
            if crm.insert_customer_data(new_customers_data, CUSTOMER_DATAFILE):
                is_success = True
                view.print_message("New customer added successfully.")
                return is_success
        else:
            if len(new_customers_data) < len(CUSTOMER_TABLE_HEADERS):
                raise IndexError("There are fields missing in customer's data. "
                                 "Try adding again providing the expected data.")
            elif len(new_customers_data) > len(CUSTOMER_TABLE_HEADERS):
                raise IndexError("Number of fields in the customer's data is higher than expected. "
                                 "Please try adding the new customer again.")
    except (IndexError, ValueError, TypeError) as error:
        is_success = False
        view.print_error_message(error)
        return is_success


def update_customer() -> bool:
    view.print_error_message("Not implemented yet.")


def delete_customer() -> bool:
    view.print_error_message("Not implemented yet.")


def list_subscribed_emails() -> bool | None:
    try:
        customer_table = crm.read_customer_data(CUSTOMER_DATAFILE)
        if customer_table is not None:
            subscribed_customers = helpers.filter_column_condition(customer_table, CUSTOMER_TABLE_INDEXES["subscribed"],
                                                                   SUBSCRIPTION_STATUSES["subscribed"])
            subscribed_customers_email = util.get_column_data(subscribed_customers, CUSTOMER_TABLE_INDEXES["email"])
            view.print_general_results(subscribed_customers_email, "Emails of subscribed customers")
            is_success = True
            return is_success
        else:
            raise TypeError("Couldn't load the customer data.")
    except (TypeError, Exception) as some_exception:
        is_success = False
        view.print_error_message(some_exception)
        return is_success


def run_operation(option) -> None:
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer(ALTERNATIVES["yes"], ALTERNATIVES["no"])
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        list_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu() -> None:
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu() -> None:
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
