```mermaid
classDiagram

    class Member {
        -int memberId
        -String name
        -String address
        -String memberType
        +placeOrder() void
        +makePayment() void
    }

    class RoyalMember {
        -double discountRate
        +orderUnavailableItem() void
    }

    class RegularMember {
        +placeOrder() void
    }

    class Order {
        -int orderId
        -Date orderDate
        -String status
        -double totalAmount
        +calculateTotal() double
        +updateStatus() void
    }

    class OrderLine {
        -int quantity
        -double lineTotal
        +calculateLineTotal() double
    }

    class Item {
        -int itemId
        -String title
        -double price
        -boolean available
        +checkAvailability() boolean
    }

    class CD {
        -String artist
    }

    class Tape {
        -int duration
    }

    class Invoice {
        -int invoiceId
        -Date issueDate
        -double amount
        +printInvoice() void
    }

    class ShippingList {
        -int shippingId
        -Date shippingDate
        +printShippingList() void
    }

    class Payment {
        -int paymentId
        -double amount
        -Date paymentDate
        +processPayment() boolean
    }

    class CashPayment {
        -String receiptNumber
        +processPayment() boolean
    }

    class CheckPayment {
        -String checkNumber
        -String bankName
        +processPayment() boolean
    }

    class BankDraftPayment {
        -String draftNumber
        +processPayment() boolean
    }

    class MembershipApplication {
        -int applicationId
        -String applicantName
        -Date applicationDate
        -String status
        +submitApplication() void
    }

    Member <|-- RoyalMember
    Member <|-- RegularMember

    Item <|-- CD
    Item <|-- Tape

    Payment <|-- CashPayment
    Payment <|-- CheckPayment
    Payment <|-- BankDraftPayment

    Member "1" --> "0..*" Order : places
    Order "1" --> "1..*" OrderLine : contains
    OrderLine "1" --> "1" Item : refers to
    Order "1" --> "0..1" Invoice : generates
    Order "1" --> "0..1" ShippingList : generates
    Order "1" --> "0..1" Payment : paid by