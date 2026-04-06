```mermaid
sequenceDiagram
    participant M as Member
    participant OPC as OrderProcessingClerk
    participant O as Order
    participant I as Item
    participant Inv as Invoice
    participant SL as ShippingList
    participant CDC as CollectionDepartmentClerk
    participant P as Payment

    M->>OPC: placeOrder(items)
    OPC->>OPC: verifyMembership(member)
    OPC->>I: checkAvailability(items)
    I-->>OPC: availability status
    OPC->>O: createOrder(items)
    O->>O: calculateTotal()
    OPC->>Inv: printInvoice(order)
    OPC->>SL: printShippingList(order)
    M->>CDC: makePayment(paymentDetails)
    CDC->>P: processPayment()
    P-->>CDC: payment accepted
    CDC-->>OPC: payment confirmed
    OPC->>O: updateStatus("confirmed")
    OPC-->>M: order confirmed