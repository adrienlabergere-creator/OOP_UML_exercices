```mermaid
classDiagram

class Member {
    -int id
    -String name
    -String address
    -String membershipType
    +placeOrder() void
    +makePayment() void
}

class Order {
    -int orderId
    -Date date
    -double totalAmount
    -String status
    +calculateTotal() double
    +updateStatus() void
}

class OrderProcessingClerk {
    -int clerkId
    -String name
    -String role
    +verifyMembership() boolean
    +processOrder() void
}

Member "1" --> "0..*" Order : places
OrderProcessingClerk "1" --> "0..*" Order : processes