def reset_database():
    initial_data = {
        "properties": {
            "P-001": {
                "propertyId": "P-001",
                "propertyNumber": "Survey #42/A",
                "location": "Downtown District, Sector 4",
                "area": "2500 sq.ft",
                "propertyType": "Commercial",
                "currentOwner": "0x1111...1111 (Owner A)",
                "documentHash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                "verified": True,
                "status": "VERIFIED",
                "registeredAt": "2026-01-10 10:00:00",
                "history": [
                    {"event": "Registered", "actor": "Authority", "timestamp": "2026-01-10 10:00:00"},
                    {"event": "Verified", "actor": "Authority", "timestamp": "2026-01-11 14:30:00"}
                ]
            },
            "P-002": {
                "propertyId": "P-002",
                "propertyNumber": "Survey #105/B",
                "location": "Greenwood Suburbs, Phase 2",
                "area": "4200 sq.ft",
                "propertyType": "Residential",
                "currentOwner": "0x2222...2222 (Owner B)",
                "documentHash": "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918",
                "verified": True,
                "status": "VERIFIED",
                "registeredAt": "2026-02-01 11:15:00",
                "history": [
                    {"event": "Registered", "actor": "Authority", "timestamp": "2026-02-01 11:15:00"},
                    {"event": "Verified", "actor": "Authority", "timestamp": "2026-02-02 09:00:00"}
                ]
            },
            "P-003": {
                "propertyId": "P-003",
                "propertyNumber": "Survey #88/C",
                "location": "Tech Park Avenue, Block C",
                "area": "1500 sq.ft",
                "propertyType": "Commercial",
                "currentOwner": "0x3333...3333 (Owner C)",
                "documentHash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                "verified": False,
                "status": "REGISTERED",
                "registeredAt": "2026-02-15 16:45:00",
                "history": [
                    {"event": "Registered", "actor": "Authority", "timestamp": "2026-02-15 16:45:00"}
                ]
            }
        }
    }
    with open(DB_PATH, "w") as f:
        json.dump(initial_data, f, indent=4)