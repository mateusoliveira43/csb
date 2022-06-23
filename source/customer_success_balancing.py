"""Module to be tested for the Technical challenge of selective process."""

from bisect import bisect

CUSTOMER = dict[str, int]
CUSTOMERS = list[CUSTOMER]


class CustomerSuccessBalancing:
    """Balance between Customer Success and Customers."""

    def __init__(
        self,
        customer_success: CUSTOMERS,
        customers: CUSTOMERS,
        customer_success_away: list[int],
    ) -> None:
        """
        Initialize balance class.

        Parameters
        ----------
        customer_success : CUSTOMERS
            List of Customers Success in company.
        customers : CUSTOMERS
            List os Customers to be served.
        customer_success_away : list[int]
            List of unavailable Customers Success.

        """
        self.customer_success = self.get_customers_sorted_by_score(
            self.get_customer_success_available(
                customer_success, customer_success_away
            )
        )
        self.customers = self.get_customers_sorted_by_score(customers)
        self.customer_success_id_most_customers = (
            self.get_customer_success_id_most_customers()
        )

    def get_customer_success_available(
        self,
        customer_success: CUSTOMERS,
        customer_success_away: list[int],
    ) -> CUSTOMERS:
        """
        Get list of Customers Success available in company.

        Parameters
        ----------
        customer_success : CUSTOMERS
            List of all Customers Success in company.
        customer_success_away : list[int]
            List of all unavailable Customers Success in company.

        Returns
        -------
        CUSTOMERS
            List of Customers Success available in company.

        """
        return [
            cs
            for cs in customer_success
            if cs["id"] not in customer_success_away
        ]

    def sort_by_score(self, customer: CUSTOMER) -> int:
        """
        Get value of key "score".

        Parameters
        ----------
        customer : CUSTOMER
            Object to sort in list.

        Returns
        -------
        int
            Value of key "score"

        """
        return customer["score"]

    def get_customers_sorted_by_score(self, customers: CUSTOMERS) -> CUSTOMERS:
        """
        Get list of Customers sorted by ascending score.

        Parameters
        ----------
        customers : CUSTOMERS
            List of Customers to be sorted.

        Returns
        -------
        CUSTOMERS
            List of Customers sorted by ascending scores.

        """
        return sorted(customers, key=self.sort_by_score)

    def serve_customers(
        self,
        customer_success: CUSTOMER,
        index: int,
    ) -> list[int]:
        """
        Serve Customers if Customer Success is able to.

        Parameters
        ----------
        customer_success : CUSTOMER
            Customer Success to be allocated.
        index : int
            Index of Customer Success sorted by ascending scores.

        Returns
        -------
        list[int]
            List of Customers' id served by Customer Success.

        """
        if index == 0:
            return [
                customer["id"]
                for customer in self.customers[
                    : bisect(
                        self.customers,
                        customer_success["score"],
                        key=self.sort_by_score,
                    )
                ]
            ]
        return [
            customer["id"]
            for customer in self.customers[
                : bisect(
                    self.customers,
                    customer_success["score"],
                    key=self.sort_by_score,
                )
            ]
            if customer["score"] > self.customer_success[index - 1]["score"]
        ]

    def balance_customer_success_and_customers(
        self,
    ) -> CUSTOMERS:
        """
        Distribute Customers for each Customer Success able to serve them.

        Returns
        -------
        CUSTOMERS
            List of dictionaries with each Customer Success' id and the number
            of Customers the person is serving.

        """
        return [
            {
                "id": customer_success["id"],
                "serving": len(
                    self.serve_customers(
                        customer_success,
                        index,
                    )
                ),
            }
            for index, customer_success in enumerate(self.customer_success)
        ]

    def get_customer_success_id_most_customers(self) -> int:
        """
        Get Id of the available Customer Success with the most Customers.

        Returns
        -------
        int
            Id of the available Customer Success with the most Customers, 0 if
            tied.

        """
        balance = sorted(
            self.balance_customer_success_and_customers(),
            key=lambda key: key["serving"],
            reverse=True,
        )
        return (
            0
            if balance[0]["serving"] == balance[1]["serving"]
            else balance[0]["id"]
        )
