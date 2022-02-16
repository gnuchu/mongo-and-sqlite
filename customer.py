class Customer:
  def __init__(self, name, address, notes, created_at):
    self.name = name
    self.address = address
    self.notes = notes
    self.created_at = created_at
  
  def to_document(self):
    return {
      "name": f"{self.name}",
      "address": f"{self.address}",
      "notes": f"{self.notes}",
      "created_at": f"{self.created_at}"
    }