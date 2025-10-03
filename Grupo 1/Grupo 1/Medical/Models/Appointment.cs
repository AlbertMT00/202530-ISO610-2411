namespace Medical.Models
{
    public class Appointment
    {
        public int Id { get; set; }
        public int PatientId { get; set; }
        public string PatientName { get; set; } = string.Empty;
        public DateTime AppointmentDate { get; set; }
        public string AppointmentTime { get; set; } = string.Empty;
        public string Doctor { get; set; } = string.Empty;
        public string Specialty { get; set; } = string.Empty;
        public string Status { get; set; } = "Programada"; // Programada, Confirmada, Completada, Cancelada
        public string Notes { get; set; } = string.Empty;
        public DateTime CreatedAt { get; set; } = DateTime.Now;
    }
}