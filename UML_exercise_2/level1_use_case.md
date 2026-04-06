```mermaid
flowchart LR

    Member[Member]
    Clerk[Order Processing Clerk]

    subgraph System[ABCD Records System]
        PlaceOrder((Place Order))
        VerifyMembership((Verify Membership))
        ProcessOrder((Process Order))
        MakePayment((Make Payment))
    end

    Member --> PlaceOrder
    Member --> MakePayment

    Clerk --> VerifyMembership
    Clerk --> ProcessOrder