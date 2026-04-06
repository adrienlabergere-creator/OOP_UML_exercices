classDiagram

    class User {
        -int id
        -String name
        -String password
        +login() boolean
        +logout() void
    }

    class Patient {
        -String email
        +submitProblem(problem: HealthProblem) void
        +receivePrescription(prescription: Prescription) void
        +makePayment(payment: Payment) void
    }

    class Doctor {
        -String specialization
        +reviewProblem(problem: HealthProblem) void
        +writePrescription(content: String) Prescription
        +receivePayment(payment: Payment) void
    }

    class Organizer {
        -boolean isAdmin
        +assignDoctor(patient: Patient, doctor: Doctor) void
        +sendPrescription(patient: Patient, prescription: Prescription) void
        +forwardPayment(payment: Payment, doctor: Doctor) void
        +createMember(user: User) void
    }

    class HealthProblem {
        -int id
        -String description
        -String status
        -Date submittedAt
        -Date updatedAt
        +updateStatus(status: String) void
    }

    class Prescription {
        -int id
        -String content
        -Date issuedAt
        +getContent() String
    }

    class Payment {
        <<abstract>>
        -int id
        -double amount
        -Date paidAt
        +process() boolean
    }

    class CheckPayment {
        -String checkNumber
        -String bankName
        +process() boolean
    }

    class CashPayment {
        -String receiptNumber
        +process() boolean
    }

    class CreditCardPayment {
        -String cardNumber
        -String expiryDate
        +process() boolean
    }

    User <|-- Patient
    User <|-- Doctor
    User <|-- Organizer

    Payment <|-- CheckPayment
    Payment <|-- CashPayment
    Payment <|-- CreditCardPayment

    Patient "1" --> "0..*" HealthProblem : submits
    HealthProblem "1" --> "0..1" Prescription : leads to
    Doctor "1" --> "0..*" HealthProblem : reviews
    Doctor "1" --> "0..*" Prescription : writes
    Organizer "1" --> "0..*" HealthProblem : manages
    Patient "1" --> "0..*" Payment : makes
    Organizer "1" --> "0..*" Payment : forwards
    Doctor "1" --> "0..*" Payment : receives
    Patient "1" --> "0..*" Prescription : history
    Prescription "0..*" --> "0..*" Prescription : references