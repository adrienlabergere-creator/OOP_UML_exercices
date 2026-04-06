```mermaid
sequenceDiagram
    participant RM as RoyalMember
    participant S as System
    participant OPC as OrderProcessingClerk
    participant CDC as CollectionDepartmentClerk

    RM->>S: placeOrder(CD1, CD2)
    S->>OPC: verifyMembership(RoyalMember)
    OPC->>S: verifyItemAvailability(CD1, CD2)
    S-->>OPC: CD1 available, CD2 unavailable
    OPC->>S: allowUnavailableItem(RoyalMember, CD2)
    OPC->>S: applyDiscount(RoyalMember)
    OPC->>S: processOrder()
    S-->>RM: printInvoice(totalAmount)
    RM->>S: makePaymentByCheck(checkDetails)
    S->>CDC: processCheckPayment(checkDetails)
    CDC-->>S: paymentAccepted
    S-->>RM: orderConfirmed