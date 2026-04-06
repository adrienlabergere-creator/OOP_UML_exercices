```mermaid
sequenceDiagram
    participant C as Customer
    participant OPC as OrderProcessingClerk
    participant M as Member
    participant MA as MembershipApplication

    C->>OPC: requestOrder()
    OPC->>M: verifyMembership(customerId)

    alt Membership valid
        M-->>OPC: membership confirmed
        OPC-->>C: order can proceed
    else Membership invalid
        M-->>OPC: membership not found
        OPC->>MA: createApplication(customerInfo)
        MA-->>OPC: application form ready
        OPC-->>C: send membership application
    end