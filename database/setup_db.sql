CREATE TABLE IF NOT EXISTS inventory_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Date TEXT NOT NULL,
    Inventory_Level INTEGER NOT NULL,
    Past_Demand INTEGER NOT NULL,
    Future_Demand INTEGER NOT NULL
);

INSERT INTO inventory_data (Date, Inventory_Level, Past_Demand, Future_Demand) VALUES
('2024-01-01', 500, 450, 470),
('2024-01-02', 520, 470, 490),
('2024-01-03', 510, 460, 480),
('2024-01-04', 495, 455, 465);
