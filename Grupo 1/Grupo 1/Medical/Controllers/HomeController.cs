using System.Diagnostics;
using Medical.Models;
using Microsoft.AspNetCore.Mvc;

namespace Medical.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            ViewBag.TotalPatients = 156;
            ViewBag.TodayAppointments = 23;
            ViewBag.PendingExams = 89;
            ViewBag.ActiveDoctors = 15;
            return View();
        }

        public IActionResult Privacy()
        {
            return View();
        }

        public IActionResult Appointments()
        {
            return RedirectToAction("Index", "Appointments");
        }

        public IActionResult MedicalHistory()
        {
            ViewBag.TotalPatients = 156;
            ViewBag.RecordCount = 892;
            return View();
        }

        public IActionResult Settings()
        {
            return View();
        }

        public IActionResult Reports()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}