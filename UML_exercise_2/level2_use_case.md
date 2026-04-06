```mermaid
flowchart LR
    Member[Member]
    NonMember[Non-Member]
    OPC[Order Processing Clerk]
    CDC[Collection Department Clerk]

    subgraph System[ABCD Records System]
        PlaceOrder((Place Order))
        VerifyMembership((Verify Membership))
        ProcessOrder((Process Order))
        MakePayment((Make Payment))
        VerifyAvailability((Verify Item Availability))
        ApplyDiscount((Apply Discount))
        PrintInvoice((Print Invoice))
        PrintShippingList((Print Shipping List))
        OrderUnavailable((Order Unavailable Items))
        SendApplication((Send Membership Application))
    end

    Member --> PlaceOrder
    Member --> MakePayment
    Member --> OrderUnavailable

    NonMember --> SendApplication

    OPC --> VerifyMembership
    OPC --> ProcessOrder
    OPC --> VerifyAvailability
    OPC --> ApplyDiscount
    OPC --> PrintInvoice
    OPC --> PrintShippingList

    CDC --> MakePayment

    ProcessOrder -. "<<include>>" .-> VerifyMembership
    ProcessOrder -. "<<include>>" .-> VerifyAvailability
    ProcessOrder -. "<<include>>" .-> PrintInvoice
    ProcessOrder -. "<<include>>" .-> PrintShippingList

    ApplyDiscount -. "<<extend>>" .-> ProcessOrder
    OrderUnavailable -. "<<extend>>" .-> PlaceOrder