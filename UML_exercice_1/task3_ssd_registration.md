```mermaid
sequenceDiagram
    participant O as Organizer
    participant S as System

    O->>S: createMember(name, role, contactInfo)
    S->>S: generateMemberId()
    S->>S: generateTemporaryPassword()
    S-->>O: memberCreated(memberId, password)