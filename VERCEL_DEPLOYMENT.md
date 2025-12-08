# PixelCipher Deployment Guide - Vercel

## Prerequisites
- GitHub account with the pixelcipher repository
- Vercel account (free tier available)
- Node.js (optional, but recommended for local testing)

## Deployment Steps

### Step 1: Prepare Your GitHub Repository
1. Ensure all changes are committed and pushed to GitHub:
   ```bash
   git add .
   git commit -m "Add Vercel configuration files"
   git push origin main
   ```

### Step 2: Connect to Vercel via GitHub
1. Go to https://vercel.com/dashboard
2. Click "Add New..." → "Project"
3. Select "Import Git Repository"
4. Find and select `mahim2909/pixelcipher`
5. Click "Import"

### Step 3: Configure Project Settings
1. **Project Name**: Keep as `pixelcipher` (or customize if desired)
2. **Environment Variables**: Add the following:
   - Key: `SECRET_KEY`
   - Value: `your-very-secret-random-string-here` (generate a secure one)
   
   - Key: `DEBUG`
   - Value: `False`

   To generate a secure SECRET_KEY, run in Python:
   ```python
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
   ```

3. **Framework**: Select "Other" (Vercel will auto-detect Python)
4. **Root Directory**: Leave as default or set to `.` (project root)

### Step 4: Configure Build Settings
In the Build & Development Settings:
- **Build Command**: `pip install -r requirements.txt`
- **Output Directory**: Leave blank
- **Install Command**: Leave blank

### Step 5: Deploy
1. Click "Deploy"
2. Wait for the build process to complete (2-5 minutes)
3. Once successful, you'll get a deployment URL like: `https://pixelcipher-xxxx.vercel.app`

## Post-Deployment Checklist

### ✅ Testing
1. Visit your deployment URL
2. Test image upload and encoding
3. Test base64 input and decoding
4. Test compression feature
5. Test image export/download

### ✅ Common Issues & Solutions

**Issue**: `ModuleNotFoundError: No module named 'django'`
- Solution: Check that requirements.txt is properly configured and build command is correct

**Issue**: Static files not loading (CSS/images not displaying)
- Solution: Vercel handles static files differently. The application serves everything through Django

**Issue**: 413 Payload Too Large error
- Solution: Vercel has a 6MB limit per function. Large images cannot be processed

**Issue**: Function timeout (>30 seconds)
- Solution: Vercel functions timeout at 30 seconds. Optimize image processing or use a dedicated server

## Environment Variables Reference

```
SECRET_KEY=your-django-secret-key
DEBUG=False
ALLOWED_HOSTS=.vercel.app,localhost,127.0.0.1
```

## Rollback & Updates

### To Rollback to Previous Deployment
1. Go to Vercel Dashboard → pixelcipher project
2. Click "Deployments"
3. Find the previous successful deployment
4. Click the three-dot menu → "Promote to Production"

### To Update After Code Changes
1. Make changes locally and commit to GitHub
2. Push to `main` branch:
   ```bash
   git push origin main
   ```
3. Vercel automatically detects changes and redeploys
4. Monitor deployment in Vercel Dashboard

## Performance Optimization Tips

1. **Image Size Limits**: 
   - Max 5MB per image recommended (for processing speed)
   - Use compression feature to reduce file sizes

2. **Database**:
   - Currently uses SQLite (suitable for Vercel)
   - For production scaling, consider PostgreSQL

3. **Caching**:
   - Vercel caches static assets automatically
   - No additional configuration needed

## Custom Domain (Optional)

1. In Vercel Dashboard → pixelcipher project
2. Go to "Settings" → "Domains"
3. Add your custom domain (e.g., pixelcipher.com)
4. Follow DNS configuration instructions

## Support & Documentation

- Vercel Django Guide: https://vercel.com/guides/using-django-with-vercel
- Django Documentation: https://docs.djangoproject.com/
- Vercel Documentation: https://vercel.com/docs

## Troubleshooting Commands

### Check Deployment Status
```bash
vercel status
```

### View Deployment Logs
Go to Vercel Dashboard → pixelcipher → Deployments → Click on deployment → View Logs

### Redeploy
```bash
vercel deploy --prod
```

---

**Note**: For production use, consider:
- Using a proper database (PostgreSQL)
- Setting up proper error logging
- Implementing rate limiting
- Adding authentication if needed
