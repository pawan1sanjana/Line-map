export default function handler(req, res) {
    const customers = [
        { id: 1, name: "John Doe", latitude: 6.9271, longitude: 79.8612 },
        { id: 2, name: "Jane Smith", latitude: 6.9147, longitude: 79.8487 },
        { id: 3, name: "Robert Brown", latitude: 6.9325, longitude: 79.8567 }
    ];
    res.status(200).json(customers);
}
