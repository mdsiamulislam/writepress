# 🚨 Render Deployment Troubleshooting Guide

## Database Connection Error Fix

The error `could not translate host name "dpg-xyz1234.ap-southeast-1.render.com"` means your Django app can't connect to the PostgreSQL database.

### ✅ Step-by-Step Fix:

#### 1. Check Your Render Dashboard

- [ ] PostgreSQL database service exists and is **Available**
- [ ] Web service exists and shows the correct repository
- [ ] Both services are in the same region

#### 2. Verify Database Configuration

Go to your PostgreSQL service in Render:

- [ ] Status shows "Available" (not "Creating" or "Failed")
- [ ] Copy the **External Database URL** - it should look like:
  ```
  postgresql://writepress:password123@dpg-abc123.ap-southeast-1.render.com/writepress
  ```

#### 3. Verify Web Service Environment Variables

In your Web Service → Environment:

- [ ] `DATABASE_URL` = Your PostgreSQL External Database URL (from step 2)
- [ ] `SECRET_KEY` = A long random string (50+ characters)
- [ ] `DEBUG` = `False`
- [ ] `RENDER_EXTERNAL_HOSTNAME` = Your app URL (optional)

#### 4. Common Issues & Solutions:

**Issue**: Database URL is wrong

- **Fix**: Make sure you copied the **External Database URL**, not Internal

**Issue**: Database not ready

- **Fix**: Wait for database status to show "Available" before deploying web service

**Issue**: Services in different regions

- **Fix**: Recreate services in the same region

**Issue**: Wrong database name/user

- **Fix**: Make sure database name and user match your render.yaml:
  - Database Name: `writepress`
  - User: `writepress`

#### 5. Deployment Commands for Render:

- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn writepress.wsgi:application`

#### 6. Force Redeploy:

If everything looks correct but still failing:

1. Go to your Web Service
2. Click "Manual Deploy" → "Deploy latest commit"
3. Watch the build logs for errors

### 🔍 How to Check Logs:

1. Go to your Web Service in Render
2. Click on "Logs" tab
3. Look for database connection errors

### 📝 Environment Variables Template:

```
DATABASE_URL=postgresql://writepress:YOUR_PASSWORD@YOUR_HOST.render.com/writepress
SECRET_KEY=your-super-secret-key-here-make-it-long-and-random
DEBUG=False
RENDER_EXTERNAL_HOSTNAME=your-app-name.onrender.com
```

### 🆘 Still Not Working?

1. Delete both services
2. Use the `render.yaml` file (recommended)
3. Create new service from repository
4. Render will auto-create both database and web service with correct linking
