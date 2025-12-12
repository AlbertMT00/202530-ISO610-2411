import multiprocessing

# Configuración básica
bind = "0.0.0.0"
timeout = 600
keepalive = 5

# Cálculo de workers (núcleos * 2 + 1)
workers = (multiprocessing.cpu_count() * 2) + 1
threads = 2

# IMPORTANTE: Usamos 'sync' (por defecto) o 'gthread' para Flask estándar.
# No uses 'uvicorn.workers.UvicornWorker' a menos que uses ASGI.
worker_class = "gthread" 

# Logs (opcional, para ver errores en Azure Log Stream)
accesslog = '-'
errorlog = '-'