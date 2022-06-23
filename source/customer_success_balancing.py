"""Module to be tested for the Technical challenge of selective process."""

from bisect import bisect

CUSTOMER = dict[str, int]
CUSTOMERS = list[CUSTOMER]
DISTRIBUTION = list[tuple[int, list[int]]]


def sort_by_score(customer: CUSTOMER) -> int:
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


def sort_list_by_score(unordered_list: CUSTOMERS) -> CUSTOMERS:
    """
    Sort a list of customers by ascending score.

    Parameters
    ----------
    unordered_list : CUSTOMERS
        List to be sorted.

    Returns
    -------
    CUSTOMERS
        Sorted list by customers' ascending scores.

    """
    return sorted(unordered_list, key=sort_by_score)


def serve_costumers(
    customer_success_by_score: CUSTOMERS,
    customers_by_score: CUSTOMERS,
    customer_success: CUSTOMER,
    index: int,
) -> list[int]:
    """
    Serve costumers if customer success is able to.

    Parameters
    ----------
    customer_success_by_score : CUSTOMERS
        List of customers success sorted by ascending scores.
    customers_by_score : CUSTOMERS
        List of customers sorted by ascending scores.
    customer_success : CUSTOMER
        Customer success to be allocated.
    index : int
        Index of customer success sorted by ascending scores.

    Returns
    -------
    list[int]
        List of customers' id served by customer success.

    """
    if index == 0:
        return [
            customer["id"]
            for customer in customers_by_score[
                : bisect(
                    customers_by_score,
                    customer_success["score"],
                    key=sort_by_score,
                )
            ]
        ]
    return [
        customer["id"]
        for customer in customers_by_score[
            : bisect(
                customers_by_score,
                customer_success["score"],
                key=sort_by_score,
            )
        ]
        if customer["score"] > customer_success_by_score[index - 1]["score"]
    ]


def distribute_customers_for_customer_success(
    customer_success_by_score: CUSTOMERS,
    customers_by_score: CUSTOMERS,
) -> DISTRIBUTION:
    """
    Distribute customers for each customer success able to.

    Parameters
    ----------
    customer_success_by_score : CUSTOMERS
        List of customers success sorted by ascending scores.
    customers_by_score : CUSTOMERS
        List of customers sorted by ascending scores.

    Returns
    -------
    DISTRIBUTION
        List of tuples with each customer success' id and the List of
        customers' id served by the person.

    """
    return [
        (
            customer_success["id"],
            serve_costumers(
                customer_success_by_score,
                customers_by_score,
                customer_success,
                index,
            ),
        )
        for index, customer_success in enumerate(customer_success_by_score)
    ]


def get_balance(distribution: DISTRIBUTION) -> int:
    """
    Get balance of customers success' serving.

    Parameters
    ----------
    distribution : DISTRIBUTION
        List of tuples with each customer success' id and the List of
        customers' id served by the person.

    Returns
    -------
    int
        Id of the available Customer Success with the most customers, 0 if
        tied.

    """
    balance = sorted(distribution, key=lambda key: len(key[1]), reverse=True)
    return 0 if len(balance[0][1]) == len(balance[1][1]) else balance[0][0]


def customer_success_balancing(
    customer_success: CUSTOMERS,
    customers: CUSTOMERS,
    customer_success_away: list[int],
) -> int:
    """
    Return the id of the Customer Success with the most customers.

    Parameters
    ----------
    customer_success : CUSTOMERS
        List of customers success from company.
    customers : CUSTOMERS
        List os customers to be served.
    customer_success_away : list[int]
        List of unavailable customers success.

    Returns
    -------
    int
        Id of the available Customer Success with the most customers, 0 if
        tied.

    """
    customer_success_available = [
        cs for cs in customer_success if cs["id"] not in customer_success_away
    ]
    customer_success_available_by_score = sort_list_by_score(
        customer_success_available,
    )
    customers_by_score = sort_list_by_score(customers)
    distribution = distribute_customers_for_customer_success(
        customer_success_available_by_score, customers_by_score
    )
    return get_balance(distribution)
