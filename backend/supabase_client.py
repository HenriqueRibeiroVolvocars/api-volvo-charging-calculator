from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFtY2ppaGp1eGpud2xnbXpkZXZsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMyOTA3NTQsImV4cCI6MjA2ODg2Njc1NH0.DVl9uph4wQUpL4Dvo2980Y-uYWc7m9dkw2K8bLAdPtU'
# SUPABASE_URL = 'https://qmcjihjuxjnwlgmzdevl.supabase.co'
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
