using Microsoft.AspNetCore.Mvc;
using Medical.Models;
using System.Collections.Generic;
using System.Linq;

namespace Medical.Controllers
{
    public class UsersController : Controller
    {
        private static List<User> _users = new List<User>
        {
            new User { 
                Id = 1, 
                FirstName = "María", 
                LastName = "González Pérez", 
                Email = "maria.gonzalez@email.com",
                Phone = "809-123-4567",
                BirthDate = new System.DateTime(1985, 5, 15),
                Gender = "Femenino",
                BloodType = "A+",
                Address = "Calle Principal #123, Santo Domingo",
                EmergencyContact = "Juan González - 809-987-6543",
                MedicalHistory = "Alergia a la penicilina"
            }
        };
        private static int _nextId = 2;

        public IActionResult Index()
        {
            return View(_users);
        }

        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Create(User user)
        {
            if (ModelState.IsValid)
            {
                user.Id = _nextId++;
                user.CreatedAt = System.DateTime.Now;
                _users.Add(user);
                TempData["SuccessMessage"] = "Paciente registrado exitosamente";
                return RedirectToAction("Index");
            }
            return View(user);
        }

        public IActionResult Edit(int id)
        {
            var user = _users.FirstOrDefault(u => u.Id == id);
            if (user == null) return NotFound();
            return View(user);
        }

        [HttpPost]
        public IActionResult Edit(int id, User user)
        {
            if (ModelState.IsValid)
            {
                var existingUser = _users.FirstOrDefault(u => u.Id == id);
                if (existingUser != null)
                {
                    existingUser.FirstName = user.FirstName;
                    existingUser.LastName = user.LastName;
                    existingUser.Email = user.Email;
                    existingUser.Phone = user.Phone;
                    existingUser.BirthDate = user.BirthDate;
                    existingUser.Gender = user.Gender;
                    existingUser.BloodType = user.BloodType;
                    existingUser.Address = user.Address;
                    existingUser.EmergencyContact = user.EmergencyContact;
                    existingUser.MedicalHistory = user.MedicalHistory;
                }
                TempData["SuccessMessage"] = "Paciente actualizado exitosamente";
                return RedirectToAction("Index");
            }
            return View(user);
        }

        public IActionResult Details(int id)
        {
            var user = _users.FirstOrDefault(u => u.Id == id);
            if (user == null) return NotFound();
            return View(user);
        }

        public IActionResult Delete(int id)
        {
            var user = _users.FirstOrDefault(u => u.Id == id);
            if (user == null) return NotFound();
            return View(user);
        }

        [HttpPost, ActionName("Delete")]
        public IActionResult DeleteConfirmed(int id)
        {
            var user = _users.FirstOrDefault(u => u.Id == id);
            if (user != null)
            {
                _users.Remove(user);
                TempData["SuccessMessage"] = "Paciente eliminado exitosamente";
            }
            return RedirectToAction("Index");
        }
    }
}