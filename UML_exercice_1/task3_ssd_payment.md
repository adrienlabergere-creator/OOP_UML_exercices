```mermaid
sequenceDiagram
    participant P as Patient
    participant S as System

    P->>S: makePayment(method, amount, paymentDetails)
    S->>S: processPayment()
    S->>S: forwardPaymentToDoctor()
    S-->>P: paymentConfirmed(receipt)