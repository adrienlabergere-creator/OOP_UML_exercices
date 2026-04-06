```mermaid
classDiagram

    class Patient {
        -int id
        -String name
        -String password
        -String email
        +submitProblem(description: String) void
        +receivePrescription() void
        +makePayment(amount: float) void
    }

    class Doctor {
        -int id
        -String name
        -String password
        -String specialization
        +reviewProblem() void
        +writePrescription(content: String) void
        +receivePayment() void
    }

    class Organizer {
        -int id
        -String name
        -String password
        -boolean isAdmin
        +assignDoctor(patient: Patient, doctor: Doctor) void
        +sendPrescription(patient: Patient) void
        +forwardPayment(doctor: Doctor) void
    }

    Organizer "1" -- "0..*" Patient : manages
    Organizer "0..*" -- "0..*" Doctor : consults