```mermaid
sequenceDiagram
    participant M as Member
    participant CDC as CollectionDepartmentClerk
    participant P as Payment
    participant Cash as CashPayment
    participant Check as CheckPayment
    participant Draft as BankDraftPayment

    M->>CDC: makePayment(method, details)

    alt Cash payment
        CDC->>Cash: processPayment()
        Cash-->>CDC: cash accepted
    else Check payment
        CDC->>Check: processPayment()
        Check-->>CDC: check accepted
    else Bank draft payment
        CDC->>Draft: processPayment()
        Draft-->>CDC: bank draft accepted
    end

    CDC-->>M: payment confirmed