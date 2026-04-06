```mermaid
sequenceDiagram
    participant P as Patient
    participant S as System
    participant O as Organizer
    participant D as Doctor

    P->>S: submitProblem(description)
    S->>O: notifyNewProblem(problem)
    O->>D: reviewProblem(problem)
    D->>D: writePrescription(content)
    D-->>O: prescription
    O-->>P: sendPrescription(prescription)
    P->>S: makePayment(paymentDetails)
    S->>O: notifyPayment(payment)
    O->>D: forwardPayment(payment)