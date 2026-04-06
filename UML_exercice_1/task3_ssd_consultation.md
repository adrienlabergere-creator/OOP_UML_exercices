```mermaid
sequenceDiagram
    participant P as Patient
    participant S as System

    P->>S: submitProblem(description)
    S->>S: createHealthProblem()
    S->>S: setStatus("pending")
    S->>S: processConsultation()
    S-->>P: deliverPrescription(prescription)