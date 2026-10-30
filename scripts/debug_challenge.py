
def parse_api_record(raw_entry: str) -> dict:
    # Simulates records: "record_id,entity_name,raw_volume,status,weight_multiplier"
    parts = raw_entry.strip().split(",")
    return {
        "id": parts[0],
        "entity": parts[1],
        "volume": float(parts[2]),
        "status": parts[3],
        "weight": float(parts[4])
    }
