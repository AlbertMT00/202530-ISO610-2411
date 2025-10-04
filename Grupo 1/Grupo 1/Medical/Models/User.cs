using System;
using System.ComponentModel.DataAnnotations;

namespace Medical.Models
{
    public class User
    {
        public int Id { get; set; }
        
        [Required(ErrorMessage = "El nombre es obligatorio")]
        public string FirstName { get; set; }
        
        [Required(ErrorMessage = "Los apellidos son obligatorios")]
        public string LastName { get; set; }
        
        [Required(ErrorMessage = "El email es obligatorio")]
        [EmailAddress(ErrorMessage = "Formato de email inválido")]
        public string Email { get; set; }
        
        [Required(ErrorMessage = "El teléfono es obligatorio")]
        public string Phone { get; set; }
        
        [Required(ErrorMessage = "La fecha de nacimiento es obligatoria")]
        public DateTime BirthDate { get; set; }
        
        [Required(ErrorMessage = "El género es obligatorio")]
        public string Gender { get; set; }
        
        [Required(ErrorMessage = "El tipo sanguíneo es obligatorio")]
        public string BloodType { get; set; }
        
        [Required(ErrorMessage = "El contacto de emergencia es obligatorio")]
        public string EmergencyContact { get; set; }
        
        [Required(ErrorMessage = "La dirección es obligatoria")]
        public string Address { get; set; }
        
        public string MedicalHistory { get; set; }
        public DateTime CreatedAt { get; set; } = DateTime.Now;
        public DateTime UpdatedAt { get; set; } = DateTime.Now; // ← AGREGAR ESTA LÍNEA
    }
}