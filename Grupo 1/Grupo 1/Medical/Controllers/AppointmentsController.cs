using Microsoft.AspNetCore.Mvc;
using Medical.Models;
using System.Collections.Generic;
using System.Linq;

namespace Medical.Controllers
{
    public class AppointmentsController : Controller
    {
        private static List<Appointment> _appointments = new List<Appointment>
        {
            new Appointment { 
                Id = 1, 
                PatientName = "María González Pérez",
                AppointmentDate = System.DateTime.Today.AddDays(1),
                AppointmentTime = "10:00 AM",
                Doctor = "Dr. Rodríguez",
                Specialty = "Cardiología",
                Status = "Confirmada"
            }
        };

        public IActionResult Index()
        {
            return View(_appointments);
        }

        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Create(Appointment appointment)
        {
            if (ModelState.IsValid)
            {
                appointment.Id = _appointments.Count + 1;
                _appointments.Add(appointment);
                TempData["SuccessMessage"] = "Cita creada exitosamente";
                return RedirectToAction("Index");
            }
            return View(appointment);
        }
    }
}