```mermaid
sequenceDiagram
    participant RM as RoyalMember
    participant OPC as OrderProcessingClerk
    participant I as Item
    participant O as Order

    RM->>OPC: placeOrder(item)
    OPC->>I: checkAvailability(item)
    I-->>OPC: unavailable

    alt Royal member privilege
        OPC->>O: createOrder(item)
        OPC->>I: reorderItem(item)
        I-->>OPC: reorder placed
        OPC->>O: updateStatus("pending restock")
        OPC-->>RM: order accepted with reorder
    else Not allowed
        OPC-->>RM: order rejected
    end